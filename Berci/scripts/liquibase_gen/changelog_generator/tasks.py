from Repository import Repository
from table import Table


def gen_drop_check_constraint_stmt(table, column):
    pass


def gen_delete_records_stmt(table, column, enum_values):
    pass


def gen_enum_constraint(table, column, enum_values):
    pass


def new_enum(repo, schema_table, column, enum_values):
    commands = []
    r = Repository(repo)
    r.add_table
    table = Table('localhost', 5433, schema_table)
    if table.is_check_constraint_on_column(column):
        commands.append(gen_drop_check_constraint_stmt(table, column))
        commands.append(gen_delete_records_stmt(table, column, enum_values))
    commands.append(gen_enum_constraint(table, column, enum_values))
    return []
