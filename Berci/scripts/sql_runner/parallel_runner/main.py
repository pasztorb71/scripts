import json
import multiprocessing

import psycopg2

import utils
from Cluster import Cluster
from utils import password_from_file, print_sql_result


def mproc_single_command_tmpl(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=password_from_file('postgres', host, port))
    cur = conn.cursor()
    cur.execute("SELECT schemaname, tablename, tableowner FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public')")
    record = cur.fetchall()
    return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record
    cur.close()
    conn.commit()
    conn.close()

def mproc_single_command_test(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=password_from_file('postgres', host, port))
    cur = conn.cursor()
    cur.execute("SELECT count(*) FROM pg_roles WHERE rolname in ('read', 'dwh_read')")
    record = cur.fetchall()
    #return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record
    return_dict[db] = record
    cur.close()
    conn.commit()
    conn.close()

def mproc_get_missing_column_comments(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=password_from_file('postgres', host, port))
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
        password=utils.password_from_file('postgres', host, port))
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
        password=password_from_file('postgres', host, port))
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
        password=password_from_file('postgres', host, port))
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
        password=password_from_file('postgres', host, port))
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
        password=password_from_file('postgres', host, port))
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
        password=password_from_file('postgres', host, port))
    cur = conn.cursor()
    recout = []
    cur.execute("SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public') "
                "and tablename not like '%$hist' order by 1,2")
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

def mproc_revoke_rights(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=password_from_file('postgres', host, port))
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
        password=password_from_file('postgres', host, port))
    cur = conn.cursor()
    #cur.execute("CREATE USER dwh_read WITH PASSWORD 'mlffTitkosPassword123!';")
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_owner = 'postgres';")
    record = cur.fetchall()
    for rec in record:
        cmd = "GRANT USAGE ON SCHEMA " + rec[0] + " TO dwh_read;"
        cur.execute(cmd)
        cmd = "GRANT " + rec[0] + "_sel TO dwh_read;"
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
            password=password_from_file('postgres', host, port))
        cur = conn.cursor()
        cur.execute("GRANT SELECT ON public.databasechangelog TO dwh_read")
        return_dict[f'{port}|{db}'] = "OK"
        cur.close()
        conn.commit()
        conn.close()
    except:
        return_dict[f'{port}|{db}'] = "Database not exists"

def start_process(target, host, port, db, return_dict):
    p = multiprocessing.Process(target=target, args=(host, port, db, return_dict))
    jobs.append(p)
    p.start()


def wait_until_end(jobs):
    for job in jobs:
        job.join()


def get_return_dict():
    manager = multiprocessing.Manager()
    return manager.dict()


def sum_counts(d):
    sum = 0
    for db, records in d.items():
        sum += records[1][0]
    return sum


def parallel_run(host, ports, databases, func):
    global jobs
    return_dict = get_return_dict()
    jobs = []
    for port in ports:
        for db in databases[0:]:
            start_process(func, host, port, db, return_dict)
    wait_until_end(jobs)
    return return_dict

def parallel_run_all_databases(host, ports, func):
    global jobs
    return_dict = get_return_dict()
    jobs = []
    for port in ports:
        env = utils.get_env(port)
        for db in utils.get_all_databases(env)[0:]:
            start_process(func, host, port, db, return_dict)
    wait_until_end(jobs)
    return return_dict


if __name__ == '__main__':
    host, port = 'localhost', 5433
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    #databases = load_from_file('../databases.txt')
    databases = cluster.databases[0:]
    #databases = ['payment_transaction']
    ports = list(range(5433,5436))
    return_dict = parallel_run(host, ports, databases, mproc_grant_dwh_read)
    print_sql_result(return_dict, len(max(databases, key=len)) + 5)

