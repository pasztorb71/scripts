import psycopg2

from utils import password_from_file


class Database:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port
        self.user = 'postgres'
        self.__conn = None

    def __repr__(self):
        return f'{self.name}__{self.port}'

    @property
    def conn(self):
        if not self.__conn:
            self.__conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.name,
                user=self.user,
                password=password_from_file(self.user, self.host, self.port))
        return self.__conn

    def sql_exec(self, *args):
        if isinstance(args[0], str):
            cmds = [args[0]]
        elif isinstance(args[0], list):
            cmds = args[0]
        self.conn.autocommit = True
        cur = self.conn.cursor()
        status = False
        while not status:
            for cmd in cmds:
                try:
                    cur.execute(cmd)
                    status = True
                    self.conn.commit()
                except psycopg2.errors.ObjectInUse as e:
                    print(e)
                    if input("Újra? [y/n]") != "y":
                        return

    def sql_executemany(self, insert_query, records):
        conn = self.conn
        cur = conn.cursor()
        status = False
        while not status:
            try:
                cur.executemany(insert_query, records)
                conn.commit()
                status = True
            except psycopg2.errors.ObjectInUse as e:
                print(e)
                if input("Újra? [y/n]") != "y":
                    return

    def sql_query(self, cmd):
        conn = self.conn
        cur = conn.cursor()
        cur.execute(cmd)
        records = cur.fetchall()
        conn.commit()
        cur.close()
        return records

    def drop_roles(self, schema):
        conn = self.conn
        cur = conn.cursor()
        cur.execute(f"SELECT rolname FROM pg_roles r WHERE r.rolname LIKE '{schema}_%'")
        records = cur.fetchall()
        for x in records:
            try:
                cur.execute(f"drop role if exists {x[0]}")
                print(f'{x[0]} role dropped.')
                conn.commit();
            except psycopg2.errors.DependentObjectsStillExist:
                conn.rollback();
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

    def truncate_all_tables(self):
        records = self.sql_query("SELECT schemaname , tablename FROM pg_catalog.pg_tables WHERE schemaname NOT IN ('public', 'pg_catalog', 'information_schema')")
        if not records:
            return
        print('A következő táblák lesznek törölve:')
        truncate_cmds = []
        for rec in records:
            print(rec[1])
            truncate_cmds.append(f'truncate table {rec[0]}.{rec[1]} CASCADE')
        if input("Mehet a törlés[y/n]") == "y":
            self.sql_exec(truncate_cmds)

    @property
    def triggers(self):
        records = self.sql_query("SELECT DISTINCT trigger_schema, trigger_name, event_object_table FROM information_schema.triggers t  WHERE trigger_name LIKE 'tr_%$hist'")
        return records

    def remove_all_hist_triggers(self):
        records = self.sql_query("SELECT DISTINCT trigger_schema, trigger_name, event_object_table FROM information_schema.triggers t  WHERE trigger_name LIKE 'tr_%$hist'")
        if not records:
            return
        print('A következő triggerek lesznek törölve:')
        truncate_cmds = []
        for rec in records:
            print(rec)
            truncate_cmds.append(f'drop trigger {rec[1]} on {rec[0]}.{rec[2]}')
        if input("Mehet a törlés[y/n]") == "y":
            self.sql_exec(truncate_cmds)

    def put_triggers(self, triggers):
        cre_cmds = []
        for trigger in triggers:
            cmd = f"call {trigger[0]}.HIST_TRIGGER_GENERATOR('{trigger[0]}', '{trigger[2]}');"
            print(cmd)
            self.sql_exec(cmd)



