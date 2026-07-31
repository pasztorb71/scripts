from classes import Environment
from classes.Repository import column_search
from MLFF.checks.global_column_search import filter_plate_number
from utils.utils_db import get_sema_from_dbname

if __name__ == '__main__':
    columns = column_search(filter_plate_number)
    with open('platenum_check.sql', 'w') as outf:
        domain = ''
        last_domain = ''
        dbname = ''
        last_dbname = ''
        schema = ''
        for col in columns:
            domain = Environment.Env.get_domain_from_dbname(col.dbname)
            dbname = col.dbname
            if domain != last_domain:
                outf.write(f'\n--- {domain}\n')
                last_domain = domain
            if dbname != last_dbname:
                outf.write(f'-- {dbname}\n')
                last_dbname = dbname
                schema = get_sema_from_dbname(dbname)
            outf.write(f'select count(*) from {schema}.{col.tabname} where {col.name} != upper({col.name});\n')
