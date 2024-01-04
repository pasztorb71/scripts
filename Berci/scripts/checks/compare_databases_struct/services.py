from Database import Database
from checks.compare_databases_struct.databases import Metadb


def write_databases_to_metadb(metadb: Metadb, dblist: list[Database]):
    database_list = []
    conn = metadb.conn
    sql = ''' INSERT INTO database(name,port) VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute('delete from database')
    for db in dblist:
        cur.execute(sql, (db.name, db.port))
    conn.commit()

