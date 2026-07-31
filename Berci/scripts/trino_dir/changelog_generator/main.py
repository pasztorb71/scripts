"""
A program táblanevek alapján legenerálja a schema_version fájlba a sorokat
"""
import os
from pathlib import Path

def infinite_counter(start: int = 0):
    """DASDASDAS"""
    n = start
    while True:
        yield n
        n += 1

def list_tables(path) -> None:
    directory_names = [name for name in os.listdir(path) if
                       os.path.isdir(os.path.join(path, name)) and name != 'masterdata_info']
    for directory in directory_names:
        print(directory)


def gen_list_from_version_xml(filename) -> list:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    started = False
    dir_tables = list()
    for line in lines:
        if '0002-acoustic_vehicle_class-create' in line:
            started = True
        if started and line == '\n':
            started = False
        if started:
            #print(line.strip())
            dirname = line.split('tables/')[1].split('/', 1)[0]
            filename = line.split(dirname + '/', 1)[1].split('"', 1)[0]
            dir_tables.append([dirname, filename])
    return dir_tables


def write_changesets(lines, ticket, v_path) -> None:
    for l in lines[:]:
        tablename = l[0]
        filename = l[1]
        seq = filename.split('-')[0]
        dirname = f"{v_path}/tables/{tablename}"
        Path(dirname).mkdir(parents=True, exist_ok=True)
        path = f"{v_path}/tables/{tablename}/{filename}"
        changeset = ("""--liquibase formatted sql
--changeset bertalan.pasztor:!seq!
--comment !ticket! !table! tábla létrehozása

""".replace('!table!', tablename).replace('!seq!', seq)).replace('!ticket!', ticket)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(changeset)


if __name__ == '__main__':
    path = "C:/GIT/AKP/data-lakehouse-trino-liquibase/liquibase/akp_masterdata"
    #list_tables(path + '/tables')
    #exit(0)
    l = gen_list_from_version_xml(path + "/versions/schema-version-0.1.0.xml")
    write_changesets(l, 'AKP-1397', path)
