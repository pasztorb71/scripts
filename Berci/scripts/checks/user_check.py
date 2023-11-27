import psycopg2

from utils import utils_sec
from sql_runner.parallel_runner.multiprocess import parallel_run_multiprocess, gen_port_databases_from_envs
from utils.utils import utils


def dwh_check(host, port, db, return_dict):
    v_user = 'dwh_stream'
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user=v_user,
            password=utils_sec.password_from_file(v_user, '*'))
    except Exception as e:
        print(f'{port}|{db}: {e}')
        return
    cur = conn.cursor()
    cur.execute("SELECT table_schema, table_name FROM information_schema.tables WHERE table_schema NOT IN ('pg_catalog', 'information_schema', 'public', 'partman')"
                "and table_name not like '%$hist'")
    record = cur.fetchall()
    tables = []
    for rec in record:
        try:
            cur.execute("select count(*) from " + rec[0] + '.' + rec[1])
            tables.append({f'{rec[1]}': 'OK'})
        except:
            tables.append({f'{rec[1]}': 'NOT OK'})
    return_dict[f'{port}|{db}'] = tables

def service_user_check(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user='postgres',
            password=utils_sec.password_from_file('postgres', port))
    except Exception as e:
        print(f'{port}|{db}: {e}')
        return
    cur = conn.cursor()
    cur.execute(f"SELECT schema_name FROM information_schema.schemata s WHERE schema_name "
                f"NOT IN ('pg_catalog', 'information_schema', 'public', 'pg_toast', 'partman', 'airflow_meta')")
    try:
        schema = cur.fetchone()[0]
    except Exception as e:
        print(f'hiba:{db}: str{e}')
    conn.close()
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user=schema+'_service',
            password=utils_sec.password_from_file(schema + '_service', host, '*'))
    except Exception as e:
        print(f'{port}|{db}: {e}')
        return
    cur = conn.cursor()
    cur.execute("SELECT schemaname, tablename  FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('pg_catalog', 'information_schema', 'public', 'partman')"
                " and tablename not like '%$hist' and tablename not in ('staging_done', 'staging_in_progress', 'staging_initial')")
    record = cur.fetchall()
    tables = []
    for rec in record:
        try:
            cur.execute(f"select count(*) from {rec[0]}.{rec[1]}")
            a = cur.fetchone()
            tables.append({f'{rec[1]}': 'OK'})
        except Exception as e:
            tables.append({f'{rec[1]}': 'NOT OK'})
            conn.rollback()
    conn.close()
    return_dict[f'{port}|{db}'] = tables


if __name__ == '__main__':
    envs = ['c_dev']
    ports_databases = gen_port_databases_from_envs(envs)[0:]
    # ports_databases = [[5741, 'postgres']]
    return_dict = parallel_run_multiprocess(ports_databases, dwh_check)
    utils.print_table_level_check(return_dict, filtered=True)