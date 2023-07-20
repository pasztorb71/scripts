import psycopg2

import utils
import utils_sec
from sql_runner.parallel_runner.main import parallel_run, gen_port_databases_from_envs, parallel_run_args


def mproc_search_in_changelog(host, port, db, return_dict, id_list):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    try:
        #cur.execute("SELECT dateexecuted FROM public.databasechangelog d WHERE upper(id) LIKE '%ADD_PRIVILEGES_TO_TABLE%' AND dateexecuted >= '2023-03-05'")
        cur.execute("SELECT dateexecuted FROM public.databasechangelog d WHERE upper(id) LIKE '%MLFFDEV-14992%' AND dateexecuted >= '2023-01-09'")
        record = cur.fetchall()
        return_dict[f'{port}|{db}'] = record
        cur.close()
        conn.commit()
        conn.close()
    except Exception as e:
        print(f'hibaaaa:{db}')
        print(str(e))


if __name__ == '__main__':
    env = 'sandbox'
    ports_databases = gen_port_databases_from_envs(env)[0:]
    # ports_databases = [[5741, 'postgres']]
    id_list = ['MLFFDEV-14556', 'MLFFDEV-14649', 'MLFFDEV-14817', 'MLFFDEV-14914']
    return_dict = parallel_run_args(ports_databases, mproc_search_in_changelog, id_list)
    utils.print_one_result(return_dict, 50)