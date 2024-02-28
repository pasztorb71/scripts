from tabulate import tabulate

from Repository import column_search


def remove_duplicates(filelist):
    keys = set()
    outlist = []
    for l in filelist:
        key = f'{l[0]}:{l[1]}:{l[2]}'
        if key not in keys and l[1] not in ['pre_ticket', 'alert_check_data']:
            keys.add(key)
            outlist.append(l)
    return outlist

def print_result(columns):
    header = ['DBNAME', 'TABLENAME', 'COLUMN', 'TYPE', 'COMMAND']
    filelist_filtered = remove_duplicates(columns)
    print(tabulate(filelist_filtered, headers=header))

def filter_plate_number(line):
    return 'plate_number ' in line and not any([x in line for x in ['COMMENT ', 'ALTER ', 'CREATE ']])

def generator_plate_number(dbname, tablename, col):
    return f"SELECT COUNT(*) || '/' || SUM(CASE WHEN length({col[0]}) > 11 THEN 1 ELSE 0 END) FROM {tablename};"

def filter_currency_constraint(line):
    return "('IDR'" in line


if __name__ == '__main__':
    print_result(column_search(filter_currency_constraint))
    #print_result(column_search(filter_plate_number, generator_plate_number))
