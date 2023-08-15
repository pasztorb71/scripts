class Column():
    def __init__(self, conn, tablename, column_name):
        self.conn = conn
        self.tabname = tablename
        self.name = column_name

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
