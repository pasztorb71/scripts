from Column import Column
from Environment import Env
from models import ForeignKey


class Table:
    def __init__(self, env, db, table):
        self.name = ''
        self.conn = Env(env).get_conn_from_db_user(db, 'postgres')
        self.schema, self.name = table.split('.')
        self.fklist = self.getfklist()

    def is_check_constraint_on_column(self, column):
        stmt = f"SELECT count(*) " \
               f"FROM pg_constraint c " \
               f"JOIN pg_attribute  a ON a.attrelid = c.conrelid " \
               f"AND a.attnum = ANY(c.conkey) " \
               f"WHERE c.conrelid = '{self.schema}.{self.name}'::regclass " \
               f"AND c.contype = 'c' " \
               f"AND a.attname = '{column}' "
        cur = self.conn.cursor()
        cur.execute(stmt)
        res = cur.fetchone()
        return res[0] == 1

    def gen_drop_constraint_stmt(self, column):
        consname = Column(self.conn, f"{self.schema}.{self.name}", column).get_constraint_name()
        return f'ALTER TABLE {self.name} DROP CONSTRAINT {consname};'

    def getfklist(self) -> list[ForeignKey]:
        stmt = f"""SELECT
                    tc.constraint_name, 
                    tc.table_name, 
                    kcu.column_name, 
                    ccu.table_name AS foreign_table_name,
                    ccu.column_name AS foreign_column_name 
                FROM 
                    information_schema.table_constraints AS tc 
                    JOIN information_schema.key_column_usage AS kcu
                      ON tc.constraint_name = kcu.constraint_name
                      AND tc.table_schema = kcu.table_schema
                    JOIN information_schema.constraint_column_usage AS ccu
                      ON ccu.constraint_name = tc.constraint_name
                      AND ccu.table_schema = tc.table_schema
                WHERE tc.constraint_type = 'FOREIGN KEY' AND tc.table_name='{self.name}'"""
        cur = self.conn.cursor()
        cur.execute(stmt)
        rows = cur.fetchall()
        return [ForeignKey(*row) for row in rows]
