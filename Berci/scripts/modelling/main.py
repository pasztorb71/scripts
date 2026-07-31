import dataclasses
from pprint import pprint

from classes.Database import Database
from modelling.sql_statements import table_names_related_to_table


@dataclasses.dataclass
class Table:
    """ Class representing a table in the database, with name and schema attributes."""
    name: str
    schema: str

def execute_sql_query(conn, query, params=None):
    with conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            res = cur.fetchall()
    return res

def get_table_names_related_to_table(conn, table_schema, table_name):
    # execute sql query with bind variables
    records = execute_sql_query(conn, table_names_related_to_table, {
        'table_name': table_name,
        'table_schema': table_schema
    })
    return [Table(name=rc[1], schema=rc[0]) for rc in records]


def get_table_names_in_schema(conn, schema_name):
        query = f"""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = '{schema_name}'
        """
        records = execute_sql_query(conn, query)
        return [rc[0] for rc in records]


if __name__ == '__main__':
    conn = Database(name='akp_be', password='postgres').conn
    tables = get_table_names_related_to_table(conn, 'akp_masterdata', 'station_x_device_x_device_unit')
    # print only names in list of Table objects in one line
    print('\n'.join([table.name for table in tables]))
