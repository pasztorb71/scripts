import psycopg2

import Environment
from utils import utils_sec
from sql_runner.parallel_runner.multiprocess import parallel_run_multiprocess
from utils.utils import get_cluster_databases, utils


def max_labels(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user='postgres',
            password=utils_sec.password_from_file('postgres', host, port))
    except Exception as e:
        print(f'{port}|{db}: {e}')
        return
    cur = conn.cursor()
    try:
        cur.execute("""SELECT
                    max( 
                      CASE  WHEN position(',' IN labels) > 0 THEN
                        split_part(labels, ',', 2) 
                        ELSE labels
                      END) labels
                     FROM public.databasechangelog 
                     WHERE labels IS NOT NULL""")
        record = cur.fetchone()[0]
    except Exception as e:
        record = ' '
    conn.close()
    return_dict[f'{port}|{db}'] = record


if __name__ == '__main__':
    env = 'test'
    databases = get_cluster_databases(env)[0:]
    #databases = Repository.get_db_names_by_group('JAKARTA')
    #databases = ['enforcement_detection']
    port = Environment.get_port_from_env_repo(env)
    ports = list(range(port, port+1))
    return_dict = parallel_run_multiprocess(ports, databases, max_labels)
    utils.print_one_result(return_dict, len(max(databases, key=len)) + 7)