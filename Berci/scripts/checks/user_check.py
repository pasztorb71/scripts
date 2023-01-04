import psycopg2

import utils
import utils_sec
from sql_runner.parallel_runner.main import parallel_run
from utils import get_cluster_databases


def dwh_check(host, port, db, return_dict):
    v_user = 'dwh_read'
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user=v_user,
            password=utils_sec.password_from_file(v_user, host, '*'))
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
            password=utils_sec.password_from_file('postgres', host, port))
    except Exception as e:
        print(f'{port}|{db}: {e}')
        return
    cur = conn.cursor()
    cur.execute("SELECT schema_name FROM information_schema.schemata s WHERE schema_name NOT IN ('pg_catalog', 'information_schema', 'public', 'pg_toast', 'partman')")
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
    env = 'new_fit'
    port = 5646
    databases = get_cluster_databases(env, port)
    #databases = Repository.get_db_names_by_group('JAKARTA')
    #databases = ['core_customer']
    #port = utils.get_port(env)
    ports = list(range(port, port+1))
    #return_dict = parallel_run(ports, databases, dwh_check)
    return_dict = parallel_run(ports, databases, service_user_check)
    utils.print_table_level_check(return_dict, filtered=True)