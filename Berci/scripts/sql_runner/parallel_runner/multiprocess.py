import multiprocessing
import os.path
from concurrent.futures import ThreadPoolExecutor
from time import sleep

import pandas as pd
import psycopg2
import yaml

import Environment
from utils import utils, utils_sec


def mproc_single_command_tmpl(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute("SELECT schemaname, tablename, tableowner FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public')")
    record = cur.fetchall()
    return_dict[f'{port}|{db}'] = [[desc[0].upper() for desc in cur.description]] + record
    cur.close()
    conn.commit()
    conn.close()

def mproc_single_sql(host, port, db, return_dict, sql):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute(sql)
    record = cur.fetchall()
    return_dict[f'{port}|{db}'] = record
    cur.close()
    conn.commit()
    conn.close()

def mproc_check_user(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user="postgres",
            password=utils_sec.password_from_file('postgres', port))
    except Exception as e:
        return_dict[f'{port}|{db}'] = str(e)
        return
    cur = conn.cursor()
    #cur.execute("SELECT count(*) FROM pg_roles WHERE rolname = 'dwh_stream'")
    cur.execute("SELECT count(*) FROM public.databasechangelog")
    #cur.execute("CREATE TABLE IF NOT EXISTS public.dbz_signal (id varchar(100) PRIMARY KEY, type varchar(32), data varchar(2048));")
    record = cur.fetchall()
    #return_dict[f'{port}|{db}'] = 'ok'
    return_dict[f'{port}|{db}'] = [[desc[0].upper() for desc in cur.description]] + record
    cur.close()
    conn.commit()
    conn.close()

def mproc_get_dabase_names(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user="postgres",
            password=utils_sec.password_from_file('postgres', port))
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database WHERE datname NOT IN ('cloudsqladmin', 'postgres', 'template0', 'template1')")
        record = cur.fetchall()
        return_dict[f'{port}|{db}'] = record
        #print(f'{port}|{db}: ok')
        cur.close()
        conn.commit()
        conn.close()
    except:
        return_dict[f'{port}|{db}'] = ("Database not exists")

def mproc_get_dabase_names_thread(port_db):
    port = port_db[0]
    db = port_db[1]
    try:
        conn = psycopg2.connect(
            host='localhost',
            port=port,
            database=db,
            user="postgres",
            password=utils_sec.password_from_file('postgres', port))
        cur = conn.cursor()
        cur.execute("SELECT datname FROM pg_database WHERE datname NOT IN ('cloudsqladmin', 'postgres', 'template0', 'template1')")
        record = cur.fetchall()
        return_dict1[f'{port}|{db}'] = record
        cur.close()
        conn.commit()
        conn.close()
    except:
        return_dict1[f'{port}|{db}'] = ("Database not exists")

def mproc_grant_after_migr(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_owner = 'postgres';")
    record = cur.fetchall()
    for rec in record:
        cur.execute(f"GRANT USAGE ON SCHEMA {rec[0]} TO  {rec[0]}_sel;")
        cur.execute(f"GRANT USAGE ON SCHEMA {rec[0]} TO  {rec[0]}_tbl_own;")
    return_dict[db] = "OK"

    cur.close()
    conn.commit()
    conn.close()

def mproc_get_missing_column_comments(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute("""select
    c.table_schema,
    c.table_name,
    c.column_name,
    pgd.description
from pg_catalog.pg_statio_all_tables as st
inner join pg_catalog.pg_description pgd on (
    pgd.objoid = st.relid
)
inner join information_schema.columns c on (
    pgd.objsubid   = c.ordinal_position and
    c.table_schema = st.schemaname and
    c.table_name   = st.relname
)
--WHERE pgd.description IS null
""")
    record = cur.fetchall()
    return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record
    cur.close()
    conn.commit()
    conn.close()



def mproc_single_csabi(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    #cur.execute("Truncate table public.debezium_heartbeat")
    #cur.execute("update public.debezium_heartbeat set last_heartbeat_ts = now()")
    try:
        cur.execute("SELECT * from public.debezium_heartbeat")
        #cur.execute("SELECT rolreplication FROM pg_roles where  rolname  = 'postgres'")
        record = cur.fetchall()
        return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record
    except psycopg2.errors.UndefinedTable:
        return_dict[db] = [['Nem létezik a tábla: public.debezium_heartbeat']]
    cur.close()
    conn.commit()
    conn.close()

def mproc_multiple_commands_tmpl(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    recout = []
    cur.execute("SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public')")
    record = cur.fetchall()
    for rec in record:
        cur.execute("select '" + rec[0] + '.' + rec[1] + "' table_name, count(*) from " + rec[0] + '.' + rec[1])
        header = [[desc[0].upper() for desc in cur.description]]
        record1 = cur.fetchall()
        recout = recout + record1
    return_dict[db] = header + recout if record else []

    cur.close()
    conn.commit()
    conn.close()

def mproc_get_missing_table_comments(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    recout = []
    cur.execute("SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public')")
    record = cur.fetchall()
    for rec in record:
        cur.execute(f"select '{rec[0]}.{rec[1]}' AS TABLE, obj_description('{rec[0]}.{rec[1]}'::regclass);")
        header = [[desc[0].upper() for desc in cur.description]]
        record1 = cur.fetchall()
        recout = recout + record1
    return_dict[db] = header + recout if record else []

    cur.close()
    conn.commit()
    conn.close()

def mproc_get_tables(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute("SELECT schemaname, tablename, tableowner FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public') and tablename not like '%$hist'")
    record = cur.fetchall()
    return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record
    cur.close()
    conn.commit()
    conn.close()

def mproc_count_tables(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute("SELECT count(*) cnt FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public')")
    record = cur.fetchall()
    return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record
    cur.close()
    conn.commit()
    conn.close()

def mproc_count_records(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    recout = []
    cur.execute(f"SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') "
                f"AND schemaname NOT IN ('public', 'information_schema', 'pg_catalog', 'airflow_meta', 'ingestion_meta') "
                f"AND tablename not like '%\_p\_%' order by 1,2")
    record = cur.fetchall()
    for rec in record:
        try:
            cur.execute(f"select '{rec[0]}' schema_name, '{rec[1]}' table_name, count(*) from {rec[0]}.{rec[1]}")
            header = [[desc[0].upper() for desc in cur.description]]
            record1 = cur.fetchall()
            recout = recout + record1
        except Exception as e:
            print(rec[0] + '.' + rec[1])
            raise e
    return_dict[f'{port}|{db}'] = header + recout if record else []

    cur.close()
    conn.commit()
    conn.close()

def truncate_table(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute(f"SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') "
                f"AND schemaname NOT IN ('public', 'information_schema', 'pg_catalog', 'airflow_meta', 'ingestion_meta') "
                f"AND tablename not like '%\_p\_%' order by 1,2")
    record = cur.fetchall()
    for rec in record:
        try:
            cur.execute(f"truncate table {rec[0]}.{rec[1]} cascade")
        except Exception as e:
            print(rec[0] + '.' + rec[1])
            raise e
        return_dict[f'{port}|{db}'] = f" {rec[0]}.{rec[1]} truncated"

    cur.close()
    conn.commit()
    conn.close()

def mproc_count_records_dataframe(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute(f"SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') "
                f"AND schemaname NOT IN ('public', 'information_schema', 'pg_catalog', 'airflow_meta', 'ingestion_meta') "
                f"AND tablename not like '%\_p\_%' order by 1,2")
    record = cur.fetchall()
    for rec in record:
        try:
            cur.execute("select '" + rec[0] + '.' + rec[1] + "' table_name, count(*) from " + rec[0] + '.' + rec[1])
            header = [[desc[0].upper() for desc in cur.description]]
            record1 = cur.fetchall()
            recout = recout + record1
        except Exception as e:
            print(rec[0] + '.' + rec[1])
            raise e
    return_dict[f'{port}|{db}'] = header + recout if record else []

    cur.close()
    conn.commit()
    conn.close()

def mproc_revoke_rights(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    recout = []
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_owner = 'postgres';")
    record = cur.fetchall()
    for rec in record:
        cmd = "REVOKE " + rec[0] + "_tbl_own FROM " + rec[0] + "_full;"
        cur.execute(cmd)
    return_dict[db] = cmd

    cur.close()
    conn.commit()
    conn.close()

def mproc_grant_dwh_read(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    try:
        cur.execute("CREATE USER dwh_read WITH PASSWORD 'mlffTitkosPassword123!';")
    except:
        conn.rollback()
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_owner = 'postgres' and schema_name != 'partman_sel';")
    record = cur.fetchall()
    for rec in record:
        cmd = "GRANT USAGE ON SCHEMA " + rec[0] + " TO dwh_read;"
        print(cmd)
        cur.execute(cmd)
        cmd = "GRANT " + rec[0] + "_sel TO dwh_read;"
        print(cmd)
        cur.execute(cmd)
    return_dict[db] = "OK"

    cur.close()
    conn.commit()
    conn.close()

def mproc_grant_hendi_read(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils_sec.password_from_file('postgres', port))
    cur = conn.cursor()
    try:
        cur.execute("CREATE USER hendipradana WITH PASSWORD 'nHY0JBGeYpQ!ayuhV';")
    except:
        conn.rollback()
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_owner = 'postgres' and schema_name != 'partman_sel';")
    record = cur.fetchall()
    for rec in record:
        cmd = "GRANT USAGE ON SCHEMA " + rec[0] + " TO hendipradana;"
        print(cmd)
        cur.execute(cmd)
        cmd = "GRANT " + rec[0] + "_sel TO hendipradana;"
        print(cmd)
        cur.execute(cmd)
    return_dict[db] = "OK"

    cur.close()
    conn.commit()
    conn.close()

def mproc_grant_dwh_read_databasechangelog(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user="postgres",
            password=utils_sec.password_from_file('postgres', port))
        cur = conn.cursor()
        cur.execute("GRANT SELECT ON public.databasechangelog TO dwh_read")
        return_dict[f'{port}|{db}'] = "OK"
        cur.close()
        conn.commit()
        conn.close()
    except:
        return_dict[f'{port}|{db}'] = "Database not exists"

def mproc_grant_dwh_stream_databasechangelog(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user="postgres",
            password=utils_sec.password_from_file('postgres', port))
        cur = conn.cursor()
        cur.execute("GRANT SELECT ON public.databasechangelog TO dwh_stream")
        return_dict[f'{port}|{db}'] = "OK"
        cur.close()
        conn.commit()
        conn.close()
    except:
        return_dict[f'{port}|{db}'] = ["Database not exists"]

def sum_counts(d):
    sum = 0
    for db, records in d.items():
        sum += records[1][0]
    return sum

def parallel_run_multiprocess(ports_dbs, func):
    host = 'localhost'
    return_dict = multiprocessing.Manager().dict()
    jobs = []
    for port_db in ports_dbs:
        p = multiprocessing.Process(target=func, args=(host, port_db[0], port_db[1], return_dict))
        jobs.append(p)
        p.start()

    # Wait until all process finish
    for job in jobs:
        job.join()
    return return_dict

def parallel_run_args(ports_dbs, func, *args):
    host = 'localhost'
    return_dict = multiprocessing.Manager().dict()
    jobs = []
    for port_db in ports_dbs:
        p = multiprocessing.Process(target=func, args=(host, port_db[0], port_db[1], return_dict, *args))
        jobs.append(p)
        p.start()
    # Wait until all process finish
    for job in jobs:
        job.join()
    return return_dict

def parallel_run_sql(ports_dbs, sql, func):
    global jobs
    host = 'localhost'
    return_dict = multiprocessing.Manager().dict()
    jobs = []
    for port_db in ports_dbs:
        p = multiprocessing.Process(target=func, args=(host, port_db[0], port_db[1], return_dict, sql))
        jobs.append(p)
        p.start()
    # Wait until all process finish
    for job in jobs:
        job.join()
    return return_dict


def gen_port_databases_from_env_db(env, databases):
    out = []
    for db in databases:
        out.append([Environment.get_port_from_env_inst(env, utils.get_instance_from_db_name(db)), db])
    return out


def is_backup():
    return os.path.isfile('../../backup/port_databases_from_envs.yaml')


def ports_databases_from_backup():
    with open('../../backup/port_databases_from_envs.yaml', 'r') as b:
        port_databases = yaml.load(b, Loader=yaml.Loader)
    return port_databases

def gen_port_databases_from_envs(envlist: list[str], forced_refresh=True):
    if not forced_refresh and is_backup():
        return ports_databases_from_backup()
    ports_databases = []
    a = []
    for env in envlist:
        a += Environment.Env(env).get_ports()
    for port in a:
        ports_databases.append([port, 'postgres'])
    return_dict = parallel_run_multiprocess(ports_databases, mproc_get_dabase_names)
    ports_databases = []
    for db, records in sorted(return_dict.items()):
        for rec in records:
            if rec[0] != "Database not exists":
                ports_databases.append([db.split('|')[0], rec[0]])
    with open('../../backup/port_databases_from_envs.yaml', 'w') as b:
        yaml.dump(ports_databases, b)
    return ports_databases


def return_dict_to_dataframe(dictproxy):
    a = list(dictproxy.keys())
    header = ['ENV', 'DB'] + dictproxy[list(dictproxy.keys())[0]][0]
    l = []
    for db, records in sorted(dictproxy.items()):
        env_db = db.split('|')
        env = Environment.get_env_name_from_port(int(env_db[0]))
        db = env_db[1]
        for rec in records[1:]:
            l.append([env, db] + list(rec))
    df = pd.DataFrame(l, columns=header)
    return df


def print_dataframe(df):
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    print(df)


if __name__ == '__main__':
    envs = ['sandbox']
    #envs = Environment.get_envs()[1:-1] #local nem kell, mlff_test nem kell
    print(envs)
    #databases = load_from_file('../databases.txt')
    #databases = ['core_customer']
    #envs = ['dev']
    ports_databases = gen_port_databases_from_envs(envs[0:1], forced_refresh=True)[0:]
    #ports_databases = [[6041, 'core_customer']]
    #return_dict = parallel_run(ports_databases, truncate_table)
    return_dict = parallel_run_multiprocess(ports_databases, mproc_count_records)
    #return_dict = parallel_run_sql(ports_databases, "SELECT md5(prosrc) FROM pg_proc WHERE proname = 'f_log_ddl'",  mproc_single_sql)
    #df = return_dict_to_dataframe(return_dict)
    #df_sorted = df.sort_values(by='COUNT', ascending=False)
    #print_dataframe(df_sorted)
    utils.print_sql_result(return_dict, 50, header=True)
    #utils.print_one_result(return_dict, 50)

