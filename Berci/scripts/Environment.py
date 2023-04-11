import utils
from Database import Database


class Env():
    def __init__(self, name):
        self.name = name

    @property
    def database_names(self):
        names = []
        for port in utils.get_ports_from_env(self.name):
            db = Database('postgres', 'localhost', str(port))
            rows = db.sql_query("SELECT datname from pg_database WHERE datistemplate IS FALSE "
                                "AND datname NOT IN ('cloudsqladmin', 'postgres')")
            names += [x[0] for x in rows]
        return names
