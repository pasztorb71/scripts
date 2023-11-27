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
    q.result[q.dbname] = header + records

def run_query_single_result_without_header(q: Querydata):
    header, records = _run_query(q)
    q.result[q.dbname] = records

def make_connection(port, database):
    conn = psycopg2.connect(
            host='localhost',
            port=port,
            database=database,
            user="postgres",
            password=utils_sec.password_from_file('postgres', 5432))
    return conn

def print_queryresult_single_value(l: list[Querydata]):
    out = []
    header = ['PORT', 'DATABASE', 'CURRENT_DATABASE']
    for q in l:
        out.append([q.port, q.dbname, q.result[q.dbname][1]])
    print(tabulate(out, headers=header))


if __name__ == "__main__":
    sql = "SELECT current_database();"
    result = {}
    l = [Querydata('5432', 'core_analytic', sql, result),
         Querydata('5432', 'core_customer', sql, result)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(run_query_single_result_with_header, l)
    print(sql)
    print_queryresult_single_value(l)
