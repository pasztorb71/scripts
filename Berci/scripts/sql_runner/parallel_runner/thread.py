import concurrent.futures
from dataclasses import dataclass

import psycopg2
from tabulate import tabulate

from utils import utils_sec

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
    q.result[f'{q.port}__{q.dbname}'] = header + records

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
    return commands[0].result


if __name__ == "__main__":
    sql = "SELECT current_database();"
    result = {}
    l = [Querydata('5432', 'core_analytic', sql, result),
         Querydata('5432', 'core_customer', sql, result)]
    result = dbcommand_thread_executor(l)
    print(result)
