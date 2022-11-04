import psycopg2

import utils
from Cluster import Cluster
from Database import Database
from sql_runner.parallel_runner.main import parallel_run, parallel_run_all_databases
from utils import get_conn, get_all_databases


def insert_into_local_all_changelogs(to_db, records, env, db):
    insert_query = """INSERT INTO public.all_changelogs_serial (env, database_name, id, author, filename, dateexecuted, 
    orderexecuted, exectype, md5sum, description, "comments", tag, liquibase, contexts, labels, deployment_id) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    to_db.sql_exec(f"delete from public.all_changelogs_serial where env='{env}' and database_name='{db}'")
    to_db.sql_executemany(insert_query, records)


def insert_proc():
    env = 'local'
    to_db = Database('postgres', 'localhost', utils.get_port(env))
    for port in range(5432, 5434):
        env = utils.get_env(port)
        print(env)
        for db in get_all_databases(env)[0:]:
            print('  ', db)
            sql = f"select '{env}', '{db}', id, author, filename, to_char(dateexecuted, 'YYYY-MM-DD HH24:MI:SS.MS'), orderexecuted, " \
                  f"exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id " \
                  f"from public.databasechangelog t"
            from_db = Database(db, 'localhost', port)
            try:
                records = from_db.sql_query(sql)
                insert_into_local_all_changelogs(to_db, records, env, db)
            except:
                pass

def insert_changelog(host, port, db, return_dict):
    env = utils.get_env(port)
    sql = f"select '{env}', '{db}', id, author, filename, to_char(dateexecuted, 'YYYY-MM-DD HH24:MI:SS.MS'), orderexecuted, " \
          f"exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id " \
          f"from public.databasechangelog t"
    try:
        from_conn = psycopg2.connect(
                host=host,
                port=port,
                database=db,
                user='postgres',
                password=utils.password_from_file('postgres', host, port))
        cur = from_conn.cursor()
        cur.execute(sql)
        records = cur.fetchall()
        from_conn.close()

        to_conn = psycopg2.connect(
                host=host,
                port=5432,
                database='postgres',
                user='postgres',
                password=utils.password_from_file('postgres', host, 5432))
        cur = to_conn.cursor()
        cur.execute(f"delete from public.all_changelogs where env='{env}' and database_name='{db}'")
        insert_query = """INSERT INTO public.all_changelogs (env, database_name, id, author, filename, dateexecuted, 
            orderexecuted, exectype, md5sum, description, "comments", tag, liquibase, contexts, labels, deployment_id) 
            VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        cur.executemany(insert_query, records)
        to_conn.commit()
        to_conn.close()
    except:
        pass

def insert_proc_parallel():
    host, port = 'localhost', 5432
    cluster = Cluster(host=host, port=port, passw=utils.password_from_file('postgres', host, port))
    # databases = load_from_file('../databases.txt')
    databases = cluster.databases[0:]
    #databases = ['enforcement_eligibility_detection']
    ports = list(range(5432, 5435))
    return_dict = parallel_run_all_databases(host, ports, insert_changelog)
    utils.print_sql_result(return_dict, len(max(databases, key=len)) + 5)


if __name__ == '__main__':
    #insert_proc()
    insert_proc_parallel()

