import psycopg2

import utils


class Database:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.user = 'postgres'

    @property
    def conn(self):
        return psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.name,
            user=self.user,
            password=utils.password_from_file(self.user, self.host, self.port))

    def sql_exec(self, cmd):
        conn = self.conn
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(cmd)
        cur.close()
        conn.close()

    def sql_query(self, cmd):
        conn = self.conn
        cur = conn.cursor()
        cur.execute(cmd)
        records = cur.fetchall()
        cur.close()
        conn.close()
        return records

    def drop_roles(self, schema):
        conn = self.conn
        cur = conn.cursor()
        cur.execute(f"SELECT rolname FROM pg_roles r WHERE r.rolname LIKE '{schema}_%'")
        records = cur.fetchall()
        for x in records:
            cur.execute(f"drop role if exists {x[0]}")
            print(f'{x[0]} role dropped.')
        conn.commit()
        cur.close()
        conn.close()

    def delete_databasechangelog(self, schema):
        conn = self.conn
        cur = conn.cursor()
        cur.execute(f"SELECT id from public.databasechangelog WHERE lower(filename) LIKE '%tariff%'")
        records = cur.fetchall()
        for x in records:
            cur.execute(f"delete from public.databasechangelog WHERE id = '{x[0]}'")
            print(f'{x[0]} id deleted from databasechangelog.')
        cur.execute(f"delete from public.databasechangelog WHERE id = 'CREATE_DATABASE-db1'")
        cur.execute(f"delete from public.databasechangelog WHERE id = 'SERVICE_USER'")
        cur.execute(f"delete from public.databasechangelog WHERE id = 'READ_USER'")
        conn.commit()
        cur.close()
        conn.close()

