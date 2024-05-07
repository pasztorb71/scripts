class Column():
    def __init__(self, dbname, tablename, column_name, type=None, conn=None,):
        self.dbname = dbname
        self.conn = conn
        self.tabname = tablename
        self.name = column_name
        self.type = type

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
