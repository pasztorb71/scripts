"""
A program az input fájlban található sql parancsokra előállítja a szkripteket az összes környezetre,
amelyeket aztán bemásol az out könyvtár alá egy (a release paraméterben megadott prefix) szerinti könyvtárba.
Ezek win bat fájlok, amelyek a környezet nevével megegyező könyvtárakban találhatók.
Az eredmény fájlok ugyanebbe a könyvtárba keletkeznek {domainnév}.sql.out fájlokba.
"""
import os
import shutil
from dataclasses import dataclass

import click
import Environment
from utils import utils_sec


@click.command()
@click.option(
        "--inputfile",
        help="File from genrate", default="databasechangelog_1_2.sql")
@click.option(
        "--release",
        help="Release", default="1.2")
def gen_plsql_scripts(inputfile, release):
    """
    :param inputfile: Az sql fájl, amiből dolgozik
    :param release: Melyik release előtt kell lefuttatni
    :return:
    """
    create_release_dir(release)
    sql = read_source_sql_file(inputfile)
    write_sql_files(release, sql)
    gen_psql_calls(release, sql)


def create_release_dir(release: str):
    path = f'out/{release}'
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir(path)
    os.mkdir(f'{path}/sql')


def read_source_sql_file(infile: str) -> dict[dict]:
    """
    It reads the file in argument and returns a dictionary with following structure:
    {
        domain_name: {
            database_name: list[command lines])
            }
    }
    :param infile:
    :return:
    """
    out = {}
    domain = ''
    db = ''
    with open(f'in/{infile}') as f:
        lines = f.read().split('\n')
    for line in lines:
        if is_domain_mark_in_line(line):
            domain = get_marker(line)
            out[domain] = {}
            db = ''
        if is_db_mark_in_line(line):
            db = get_marker(line)
            if db not in out[domain].keys():
                out[domain][db] = []
        if line and not is_db_mark_in_line(line):
            if domain and db:
                try:
                    out[domain][db].append(line)
                except Exception as e:
                    pass
    return out


def is_domain_mark_in_line(line: str) -> bool:
    return line.startswith('---')


def is_db_mark_in_line(line: str) -> bool:
    return line.startswith('-- ')


def get_marker(line):
    return line.split(' ')[1]


def write_sql_files(release, sql):
    for domain, db_dict in sql.items():
        if not any([i for i in db_dict.values()]):
            continue
        with open(f'out/{release}/sql/{domain}.sql', 'w') as f:
            for db, sqls in db_dict.items():
                if sqls:
                    f.write(f'\c {db}\n')
                    f.write('\n'.join(sqls) + '\n\n')


def gen_psql_calls(release, sql):
    envs = Environment.Env.get_envs(exclude=['mlff_test'])
    l = os.listdir(f'out/{release}/sql')
    for env in envs[0:]:
        print(env)
        os.mkdir(f'out/{release}/{env}')
        baseport = Environment.Env._env_ports[env]
        f = open(f'out/{release}/{env}/run_psql_{env}.bat', 'w')
        passw = utils_sec.password_from_file('postgres', baseport)
        f.write(f'@SET PGPASSWORD={passw}\n')
        for domain in l:
            offset = Environment.Env._domain_offsets[domain.split('.')[0]]
            if env == 'local':
                passw = 'postgres'
                baseport = 5432
                offset = 0
            f.write(f'psql -p {(baseport + offset)} -U postgres -d postgres -a -f ../sql/{domain} >{domain}.out \n')


if __name__ == '__main__':
    gen_plsql_scripts()
