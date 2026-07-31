import trino

class Trino_class:
	""" Trino database connection and query execution class. """
	def __init__(self, host=None, port=None, user=None, catalog=None, schema=None):
		self.conn = trino.dbapi.connect(
			host=host,  # e.g., 'localhost' or IP / domain
			port=port,  # default Trino port
			user=user,  # required
			catalog=catalog,  # e.g. 'hive', 'postgresql', etc.
			schema=schema,  # e.g. 'default'
		)
		self.rows = None
		self.cursor = self.conn.cursor()

	def execute_query(self, query: str):
		self.cursor.execute(query)
		self.rows = self.cursor.fetchall()

	def query(self, query: str):
		self.execute_query(query)
		return self.rows

	def get_ddl(self, tablename: str) -> str:
		""" Get the DDL of a table. """
		self.execute_query(f"SHOW CREATE TABLE {tablename}")
		ddl = self.rows[0][0]
		return ddl

