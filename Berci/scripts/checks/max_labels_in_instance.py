import psycopg2

from classes import Environment
from utils import utils_sec, utils
from sql_runner.parallel_runner.multiprocess import parallel_run_multiprocess


def max_labels(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user='postgres',
            password=utils_sec.password_from_file('postgres', port, host))
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
    env = 'cantas_prod'
    ports_databases = Environment.Env(env).gen_port_databases([env], forced_refresh=True)[0:]
    #databases = Repository.get_db_names_by_group('JAKARTA')
    #databases = ['enforcement_detection']
    return_dict = parallel_run_multiprocess(ports_databases, max_labels)
    #utils.print_dict_to_file(return_dict, 'out/max_labels.txt')
    a = return_dict.keys()
    le = [len(x) for x in return_dict.keys()]
    utils.print_one_result(return_dict, (max(le) + 7))