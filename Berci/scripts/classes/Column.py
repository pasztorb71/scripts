class Column():
    def __init__(self, dbname, tablename, column_name, type=None, conn=None, schema=None):
        self.dbname = dbname
        self.conn = conn
        self.tabname = tablename
        self.name = column_name
        self.type = type
        self.schema = schema

    def __str__(self):
        return f'{self.dbname}: {self.tabname}.{self.name}'

    def __eq__(self, other):
        return (self.dbname, self.tabname, self.name, self.type) == (other.dbname, other.tabname, other.name, other.type)

    def get_constraint_name(self):
        stmt = f"SELECT conname " \
               f"FROM pg_constraint c " \
               f"JOIN pg_attribute  a ON a.attrelid = c.conrelid " \
               f"AND a.attnum = ANY(c.conkey) " \
               f"WHERE c.conrelid = '{self.tabname}'::regclass " \
               f"AND c.contype != 'p' " \
               f"AND a.attname = '{self.name}' "
        cur = self.conn.cursor()
        cur.execute(stmt)
        res = cur.fetchone()
        return res[0]

    @property
    def nullable(self):
        stmt = (f"SELECT is_nullable "
                f"FROM information_schema.COLUMNS "
                f"WHERE table_name = '{self.tabname}' AND column_name = '{self.name}'")
        cur = self.conn.cursor()
        cur.execute(stmt)
        res = cur.fetchone()
        return res[0]

    @property
    def count_values(self):
        stmt = (f"SELECT {self.name}, count(*) FROM {self.schema}.{self.tabname} group by 1")
        cur = self.conn.cursor()
        cur.execute(stmt)
        res = cur.fetchall()
        if res:
            return res
        return None
