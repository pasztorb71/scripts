import psycopg2

from Cluster import Cluster
from Repository import Repository
from sql_runner.parallel_runner.main import parallel_run
from utils import password_from_file


def get_changelogs(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password='fLXyFS0RpmIX9uxGII4N')

    cur = conn.cursor()
    cur.execute("""SELECT DISTINCT st FROM (
SELECT 
substring(id FROM 'DDL-(.*)-MLFFDEV') st
--* 
FROM databasechangelog d 
) s
WHERE st IS NOT null;""")
    record = cur.fetchall()
    if record:
        num = max([int(x[0].split('.')[1]) for x in record])
    else:
        num = None
    return_dict[db] = num
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    host, port = 'localhost', 5434
    cluster = Cluster(host=host, port=port, passw=password_from_file(host, port))
    #databases = load_from_file('../databases.txt')
    databases = cluster.databases[0:]
    #databases = ['core_customer']
    return_dict = parallel_run(host, port, databases, get_changelogs)
    for db, records in return_dict.items()[0:]:
        print(f"{db}: {str(records)}")

