import json
import multiprocessing

import psycopg2

import utils
import utils_sec
from Cluster import Cluster
import utils
from utils_sec import password_from_file


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

def mproc_get_dabase_names(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=password_from_file('postgres', port))
    cur = conn.cursor()
    cur.execute("SELECT datname FROM pg_database WHERE datname NOT IN ('cloudsqladmin', 'postgres', 'template0', 'template1')")
    record = cur.fetchall()
    return_dict[f'{port}|{db}'] = record
    cur.close()
    conn.commit()
    conn.close()

def mproc_grant_after_migr(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=password_from_file('postgres', host, port))
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
        password=utils_sec.password_from_file('postgres', host, port))
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
        password=password_from_file('postgres', port))
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
    cur.execute("SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public', 'information_schema', 'pg_catalog') "
                " order by 1,2")
    record = cur.fetchall()
    for rec in record:
        cur.execute("select '" + rec[0] + '.' + rec[1] + "' table_name, count(*) from " + rec[0] + '.' + rec[1])
        header = [[desc[0].upper() for desc in cur.description]]
        record1 = cur.fetchall()
        recout = recout + record1
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

def sum_counts(d):
    sum = 0
    for db, records in d.items():
        sum += records[1][0]
    return sum

def parallel_run(ports_dbs, func):
    global jobs
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


def gen_port_databases_from_env_db(env, databases):
    out = []
    for db in databases:
        out.append([utils.get_port_from_env_inst(env, utils.get_instance_from_db_name(db)), db])
    return out

def gen_port_databases_from_env(env):
    ports_databases = []
    a = utils.get_ports_from_env(env)
    for port in a:
        ports_databases.append([port, 'postgres'])
    return_dict = parallel_run(ports_databases, mproc_get_dabase_names)
    ports_databases = []
    for db, records in sorted(return_dict.items()):
        for rec in records:
            ports_databases.append([db.split('|')[0], rec[0]])
    return ports_databases

if __name__ == '__main__':
    env = 'new_train'
    #databases = load_from_file('../databases.txt')
    #databases = ['core_customer']
    ports_databases = gen_port_databases_from_env(env)[0:]
    #ports_databases = [[5741, 'postgres']]
    return_dict = parallel_run(ports_databases, mproc_get_dabase_names)
    utils.print_sql_result(return_dict, 50, header=True)

