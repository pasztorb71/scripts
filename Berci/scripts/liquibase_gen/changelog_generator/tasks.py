from table import Table


def new_enum(host, port, table, column, enum_values):
    commands = []
    table = Table(host, port, table)
    if table.is_check_constraint_on_column(column):
        commands.append(gen_drop_check_constraint_stmt(table, column))
        commands.append(gen_delete_records_stmt(table, column, enum_values))
    commands.append(gen_enum_constraint(table, column, enum_values))
    return []
