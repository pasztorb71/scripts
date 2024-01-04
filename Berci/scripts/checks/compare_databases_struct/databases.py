import sqlite3
from abc import ABC
from sqlite3 import Error


class Metadb(ABC):
    def __init__(self, file):
        self.file = file
        self.conn = self.create_connection()

    def create_connection(self):
        pass

class sqlite_metadb(Metadb):
    def create_connection(self):
        """ create a database connection to a SQLite database """
        conn = None
        try:
            conn = sqlite3.connect(self.file)
        except Error as e:
            print(e)
        return conn

    def read_databases(self):
        database_list = []
        conn = self.conn
        sql = ''' SELECT env, name, port FROM database '''
        cur = conn.cursor()
        cur.execute(sql)
        out = cur.fetchall()
        conn.commit()
        return out
