import psycopg2

import Environment
import utils
import utils_sec
from Database import Database
from checks.db_changeset_status import get_changeset_ids_from_repos_release
from sql_runner.parallel_runner.main import parallel_run, gen_port_databases_from_envs
from Repository import get_repos_containing_release


def insert_into_local_all_changelogs(to_db, records, env, db):
    insert_query = """INSERT INTO public.all_changelogs_serial (env, database_name, id, author, filename, dateexecuted, 
    orderexecuted, exectype, md5sum, description, "comments", tag, liquibase, contexts, labels, deployment_id) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    to_db.__sql_exec(f"delete from public.all_changelogs_serial where env='{env}' and database_name='{db}'")
    to_db.sql_executemany(insert_query, records)


def insert_proc():
    env = 'local'
    to_db = Database('postgres', 'localhost', Environment.get_port_from_env_repo(env))
    for port in range(5432, 5434):
        env = utils.get_env_old(port)
        print(env)
        for db in Environment.Env(env).get_all_databases()[0:]:
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
    env = Environment.Env.get_env_name_from_port(port)
    sql = f"select '{env}', '{db}', id, author, filename, to_char(dateexecuted, 'YYYY-MM-DD HH24:MI:SS.MS'), orderexecuted, " \
          f"exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id " \
          f"from public.databasechangelog t"
    from_conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user='postgres',
            password=utils_sec.password_from_file('postgres', port))
    cur = from_conn.cursor()
    cur.execute(sql)
    records = cur.fetchall()
    from_conn.close()

    to_conn = psycopg2.connect(
            host=host,
            port=5432,
            database='postgres',
            user='postgres',
            password=utils_sec.password_from_file('postgres', 5432))
    cur = to_conn.cursor()
    cur.execute(f"delete from public.all_changelogs where env='{env}' and database_name='{db}'")
    insert_query = """INSERT INTO public.all_changelogs (env, database_name, id, author, filename, dateexecuted, 
        orderexecuted, exectype, md5sum, description, "comments", tag, liquibase, contexts, labels, deployment_id) 
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    cur.executemany(insert_query, records)
    to_conn.commit()
    to_conn.close()


def insert_proc_parallel(env):
    ports_databases = gen_port_databases_from_envs(env)[0:]
    print('Insert start...')
    return_dict = parallel_run(ports_databases, insert_changelog)
    utils.print_sql_result(return_dict, 50)



def insert_filesystem_all_changelogs():
    repos = get_repos_containing_release('')
    changeset_ids = get_changeset_ids_from_repos_release(repos, '')
    for db, values in changeset_ids.items():
        file_label = next(iter(values))
        file = file_label.split('||')[0]
        label = file_label.split('||')[1]
        pass
    pass

if __name__ == '__main__':
    #TODO a id LIKE '%MLFFDEV-22171%' miért került bele a cantas_test-be?
    envs = Environment.get_envs()
    envs = ['sandbox']
    print('Envs:')
    print('  -'+ '\n  -'.join(envs))
    insert_proc_parallel(envs[0:])

