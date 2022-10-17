import psycopg2
from tabulate import tabulate

import utils
from Cluster import Cluster
from sql_runner.parallel_runner.main import parallel_run
from utils import get_env

def dwh_check(host, port, db, return_dict):
    v_user = 'dwh_read'
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user=v_user,
        password=utils.password_from_file(v_user, host, '*'))
    cur = conn.cursor()
    recout = []
    cur.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema NOT IN ('pg_catalog', 'information_schema', 'public')")
    record = cur.fetchall()
    for rec in record:
        cur.execute("select '" + rec[0] + '.' + rec[1] + "' table_name, count(*) from " + rec[0] + '.' + rec[1])
        header = [[desc[0].upper() for desc in cur.description]]
        record1 = cur.fetchall()
        recout = recout + record1
    return_dict[db] = header + recout if record else []

if __name__ == '__main__':
    version_files = {}
    header = []
    result_d = {}
    result_l = []
    for port in range(5433, 5434):
        host = 'localhost'
        header.append(get_env(port))
        cluster = Cluster(host=host, port=port, passw=utils.password_from_file('postgres', host, port))
        databases = cluster.databases[0:]
        #databases = ['payment_psp_clearing']
        return_dict = parallel_run(host, port, databases, dwh_check)
        for key, data in return_dict.items():
            if key not in result_d:
                result_d[key] = [data]
            else:
                result_d[key].append(data)
        print(f"{get_env(port)}: OK")
    for i in result_d.items():
        result_l.append([i[0]])
        idx = len(result_l) - 1
        result_l[idx] += i[1]
    utils.print_sql_result(return_dict)