from Repository import Repository
from table import Table



def new_enum(repo, schema_table, column, enum_values):
    commands = []
    db = Repository(repo).get_db_name()
    table = Table('local', db, schema_table)
    if table.is_check_constraint_on_column(column):
        commands.append(table.gen_drop_check_constraint_stmt(column))
        commands.append(table.gen_delete_records_stmt(column, enum_values))
    commands.append(table.gen_enum_constraint(column, enum_values))
    return []
