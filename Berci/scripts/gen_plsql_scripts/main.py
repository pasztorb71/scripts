"""
A program az input fájlban található sql parancsokra előállítja a szkripteket az összes környezetre,
amelyeket aztán bemásol egy (a release paraméterben megadott prefix) szerinti könyvtárba.
"""
import os
import shutil

import click

import Environment
from utils import utils_file, utils_sec




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
    #utils_file.copy_dir('template', f'out/{release}', delete_dir_if_exists=True)
    create_release(release)
    sql = read_source_sql_file()
    write_sql_files(release, sql)
    gen_psql_calls(release, sql)

def create_release(release):
    path = f'out/{release}'
    if os.path.isdir(path) == True:
        shutil.rmtree(path)
    os.mkdir(path)
    os.mkdir(f'{path}/sql')

def read_source_sql_file() -> dict[dict]:
    out = {}
    env = ''
    db = ''
    with open('in/databasechangelog_1_2.sql') as f:
        lines = f.read().split('\n')
    for line in lines:
        if line.startswith('---'):
            env = line.split(' ')[1]
            out[env] = {}
        if line.startswith('-- '):
            db = line.split(' ')[1]
            if db not in out[env].keys():
                out[env][db] = []
        if line and not line.startswith('--'):
            if env and db:
                out[env][db].append(line)
    return out

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