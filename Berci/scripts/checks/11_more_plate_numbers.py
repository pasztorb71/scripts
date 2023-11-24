import glob

from tabulate import tabulate

from utils.utils_db import get_db_name


def remove_duplicates(filelist):
    keys = set()
    outlist = []
    for l in filelist:
        key = f'{l[0]}:{l[1]}:{l[2]}'
        if key not in keys and l[1] not in ['pre_ticket', 'alert_check_data']:
            keys.add(key)
            outlist.append(l)
    return outlist



if __name__ == '__main__':
    filelist = []
    for name in glob.glob('c:/GIT/MLFF/**/*.sql', recursive = True):
        with open(name, 'r') as f:
            for line in f.readlines():
                if 'plate_number ' in line and not any([x in line for x in ['COMMENT ','ALTER ','CREATE ']]):
                    repo_name = name.split('\\')[1]
                    dbname = get_db_name(name)
                    print(repo_name)
                    print(repo_name)
                    tablename = name.split('\\tables\\')[1].split('\\')[0]
                    print(tablename)
                    col = line.split()
                    print(col[0], col[1])
                    command = f"SELECT COUNT(*) || '/' || SUM(CASE WHEN length({col[0]}) > 11 THEN 1 ELSE 0 END) FROM {tablename};"
                    filelist.append([dbname, tablename, col[0], col[1], command])
    header = ['DBNAME', 'TABLENAME', 'COLUMN', 'TYPE', 'COMMAND']
    filelist_filtered = remove_duplicates(filelist)
    print(tabulate(filelist_filtered, headers=header))
