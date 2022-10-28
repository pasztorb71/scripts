import utils
from Database import Database
from utils import get_conn, get_all_databases


def insert_into_local_all_changelogs(to_db, records, env, db):
    insert_query = """INSERT INTO public.all_changelogs (env, database_name, id, author, filename, dateexecuted, 
    orderexecuted, exectype, md5sum, description, "comments", tag, liquibase, contexts, labels, deployment_id) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
    to_db.sql_exec(f"delete from public.all_changelogs where env='{env}' and database_name='{db}'")
    to_db.sql_executemany(insert_query, records)


if __name__ == '__main__':
    env = 'local'
    to_db = Database('postgres', 'localhost', utils.get_port(env))
    for port in range(5433, 5434):
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

