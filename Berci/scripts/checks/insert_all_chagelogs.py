from Cluster import Cluster
from utils import password_from_file, get_conn


def get_databases():
    host, port = 'localhost', 5434
    cluster = Cluster(host=host, port=port, passw=password_from_file(host, port))
    return cluster.databases


if __name__ == '__main__':
    db = get_databases()[0]
    env = 'dev'
    conn = get_conn(env, db, 'postgres')
    cur = conn.cursor()
    sql = f"select '{env}', '{db}', id, author, filename, to_char(dateexecuted, 'YYYY-MM-DD HH24:MI:SS.MS'), orderexecuted, " \
          f"exectype, md5sum, description, comments, tag, liquibase, contexts, labels, deployment_id " \
          f"from public.databasechangelog t"
    cur.execute(sql)
    records = cur.fetchall()
    for r in records:
        print(r)

    conn1 = get_conn('local', 'postgres', 'postgres')
    cur1 = conn1.cursor()

    insert_query = """INSERT INTO public.all_changelogs (env, database_name, id, author, filename, dateexecuted, 
    orderexecuted, exectype, md5sum, description, "comments", tag, liquibase, contexts, labels, deployment_id) 
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""

    cur1.executemany(insert_query, records)
    conn1.commit()
