import concurrent.futures
from dataclasses import dataclass

import psycopg2

from classes import Environment
from utils import utils_sec, utils


@dataclass
class Querydata:
    port: int
    dbname: str
    sql: str
    result: {}

def _run_query(q: Querydata):
    conn = make_connection(q.port, q.dbname)
    cur = conn.cursor()
    cur.execute(q.sql)
    records = cur.fetchall()
    header = [desc[0].upper() for desc in cur.description]
    return (header, records)

def run_query_single_result_with_header(q: Querydata):
    header, records = _run_query(q)
    q.result[f'{q.port}__{q.dbname}'] = [header] + records

def run_query_single_result_without_header(q: Querydata):
    header, records = _run_query(q)
    q.result[f'{q.port}__{q.dbname}'] = records

def make_connection(port, database):
    conn = psycopg2.connect(
            host='localhost',
            port=port,
            database=database,
            user="postgres",
            password=utils_sec.password_from_file('postgres', port))
    return conn

def dbcommand_thread_executor(commands: list[Querydata]) -> dict[str, list]:
    """commands = list of Querydata
    Querydata('port', database_name, sql_command, result_dict"""
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(run_query_single_result_without_header, commands)


if __name__ == "__main__":
    sql = """CREATE TEMPORARY TABLE t (
              schemaname TEXT,
              tablename TEXT,
              count int8
            );
            DO $$
            DECLARE 
              rec record;
              cmd TEXT;
            BEGIN 
              FOR rec IN SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') 
                              AND schemaname NOT IN ('public', 'ddl_changes', 'partman', 'pg_catalog', 'information_schema') 
                              and tablename not like '%$hist%'
                              and tablename not like '%\_p2%'
                              AND tablename != 't'
              LOOP 
                cmd := 'INSERT INTO t SELECT '''||rec.schemaname||''','''||rec.tablename||''', count(*) FROM '||rec.schemaname||'.'||rec.tablename;
                RAISE NOTICE '%', cmd;
                execute cmd;  
              END LOOP;
            END$$;
            SELECT * FROM t"""
    result = {}
    ports_databases = Environment.Env.gen_port_databases(['local'], forced_refresh=True)[0:]
    l = [Querydata(x[0], x[1], sql, result) for x in ports_databases]
    dbcommand_thread_executor(l)
    utils.print_sql_result(result, maxlength=50, header=True)