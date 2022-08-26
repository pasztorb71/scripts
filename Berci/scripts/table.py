from utils import get_conn


class Table:
    def __init__(self, env, table):
        self.conn = get_conn(env)
        self.schema, self.name = table.split('.')

    def is_check_constraint_on_column(column):
        pass
