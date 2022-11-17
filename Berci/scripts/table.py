from Column import Column
from utils import get_conn

class Table:
    def __init__(self, env, db, table):
        self.table = table
        self.conn = get_conn(env, db, 'postgres')
        self.schema, self.name = table.split('.')

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
        consname = Column(self.conn, self.table, column).get_constraint_name()
        return f'ALTER TABLE {self.name} DROP CONSTRAINT {consname};'