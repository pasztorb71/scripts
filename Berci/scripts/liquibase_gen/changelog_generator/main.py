import os
from pprint import pprint

def infinite_counter(start: int = 0):
    n = start
    while True:
        yield n
        n += 1

def list_tables():
    global path, name
    path = r'c:/GIT/AKP/data-backend-database-postgres-liquibase/liquibase/masterdata/tables'
    directory_names = [name for name in os.listdir(path) if
                       os.path.isdir(os.path.join(path, name)) and name != 'masterdata_info']
    seq = infinite_counter(33)
    for directory in directory_names:
        print(directory)


def gen_list():
    filename = "C:/GIT/AKP/data-backend-database-postgres-liquibase/liquibase/masterdata/versions/schema-version-0.1.0.xml"
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    started = False
    dir_tables = list()
    for line in lines:
        if '0033-measurement_class-add-trigger.sql' in line:
            started = True
        if started and line == '\n':
            started = False
        if started:
            #print(line.strip())
            dirname = line.split('tables/')[1].split('/', 1)[0]
            filename = line.split(dirname + '/', 1)[1].split('"', 1)[0]
            dir_tables.append([dirname, filename])
    return dir_tables


def write_files(lines):
    for l in lines[:]:
        tablename = l[0]
        filename = l[1]
        seq = filename.split('-')[0]
        path = f"C:/GIT/AKP/data-backend-database-postgres-liquibase/liquibase/masterdata/tables/{tablename}/{filename}"
        changeset = """--liquibase formatted sql
--changeset bertalan.pasztor:!seq!
--comment AKP-854 measurement_info trigger létrehozása
SET search_path = ${schema_name_new};

CALL public.measurement_info_trigger_generator('${schema_name_new}', '!table!');

COMMIT;
""".replace('!table!', tablename).replace('!seq!', seq)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(changeset)


if __name__ == '__main__':
    #list_tables()
    l = gen_list()
    write_files(l)

