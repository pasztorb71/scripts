"""
A program az input fájlban található sql parancsokra előállítja a szkripteket az összes környezetre,
amelyeket aztán bemásol az out könyvtár alá egy (a release paraméterben megadott prefix) szerinti könyvtárba.
Ezek win bat fájlok, amelyek a környezet nevével megegyező könyvtárakban találhatók.
Az eredmény fájlok ugyanebbe a könyvtárba keletkeznek {domainnév}.sql.out fájlokba.
"""
import os
import shutil
import click
import Environment
from utils import utils_sec


@click.command()
@click.option(
        "--inputfile",
        help="File generate from", default="qa_write_cantas.sql")
@click.option(
        "--release",
        help="Release", default="qa_write_cantas")
def gen_plsql_scripts(inputfile, release):
    """
    :param inputfile: Az sql fájl, amiből dolgozik
    :param release: Melyik release előtt kell lefuttatni
    :return:
    """
    sql = read_source_sql_file(inputfile)
    if input("Mehet a törlés? [y/n]") == "y":
        create_release_dir(release)
        write_sql_files(release, sql)
        write_psql_calls_to_file(release, sql)
    else:
        print('Csak a db szerinti szkriptgenerálás fut...')
    write_sql_files_bydb(release, sql)
    write_psql_calls_bydb_to_file(release, sql)


def get_dbname_from_update(cmd):
    splitted = cmd.lower().replace(' ', '').split('filename=')
    dirty_dbname = splitted[1].split('/')[0]
    return dirty_dbname.replace("'",'')


def get_dbname_from_insert(cmd):
    values = cmd.lower().replace(' ', '').split('values')
    dirty_dbname = values[1].split(',')[2].split('/')[0]
    return dirty_dbname.replace("'", '')


def get_dbnames_from_postgres_command(commands) -> set[str]:
    dbnames = set()
    commandlist = [x for x in ''.join(commands).split(';') if x]
    for cmd in commandlist:
        if 'UPDATE ' in cmd.upper():
            dbname = get_dbname_from_update(cmd)
            dbnames.add(dbname)
        if 'INSERT INTO ' in cmd.upper():
            dbname = get_dbname_from_insert(cmd)
            dbnames.add(dbname)
    return dbnames


def get_database_names(sql):
    dbnames = set()
    for domain, data in sql.items():
        for dbname, commands in data.items():
            if dbname == 'postgres':
                _dbnames = get_dbnames_from_postgres_command(commands)
                dbnames.update(_dbnames)
            else:
                dbnames.add(dbname)
    return dbnames


def filter_domain_from_sql(sql, dbname):
    ret = {}
    for domain, data in sql.items():
        if dbname.startswith(domain):
            return data
    return ret


def convert_to_str_commands(commands: list) -> list:
    return '\n'.join(commands).split(';\n')


def get_db_filtered_commands_for_postgresdb(filtered_domain: dict, dbname):
    commands = []
    if 'postgres' not in filtered_domain.keys():
        return []
    str_commands = convert_to_str_commands(filtered_domain['postgres'])
    for command in str_commands:
        if f'{dbname}/' in command:
            commands.append(command)
    return commands


def get_db_filtered_commands_for_pdb(filtered_domain: dict, dbname):
    commands = []
    str_commands = convert_to_str_commands(filtered_domain[dbname])
    for command in str_commands:
        if f'{dbname}/' in command:
            commands.append(command)
    return commands

def write_db_commands_to_sql_file(postresdb_commands, pdb_commands, filename, dbname):
    with open(filename, 'w') as f:
        if postresdb_commands:
            f.write('\c postgres\n')
            f.write(';\n'.join(postresdb_commands))
            f.write('\n\n')
        f.write(f'\c {dbname}\n')
        f.write(';\n'.join(pdb_commands))
        f.write('\n')


def write_sql_files_bydb(release, sql):
    db_names= get_database_names(sql)
    for dbname in sorted(db_names):
        bat_filename = f'out/{release}/sql_bydb/run_psql_{dbname}.bat'
        sql_filename = f'out/{release}/sql_bydb/{dbname}.sql'
        filtered_domain = filter_domain_from_sql(sql, dbname)
        postresdb_commands = get_db_filtered_commands_for_postgresdb(filtered_domain, dbname)
        pdb_commands = get_db_filtered_commands_for_pdb(filtered_domain, dbname)
        write_db_commands_to_sql_file(postresdb_commands, pdb_commands, sql_filename, dbname)


def create_bat_file_for_database(env, release, dbname, filename):
    baseport = Environment.Env._env_ports[env]
    with open(filename, 'w') as f:
        passw = utils_sec.password_from_file('postgres', baseport)
        f.write(f'@SET PGPASSWORD={passw}\n\n')


def create_release_dir(release: str):
    path = f'out/{release}'
    if os.path.isdir(path):
        shutil.rmtree(path)
    os.mkdir(path)
    os.mkdir(f'{path}/sql')
    os.mkdir(f'{path}/sql_bydb')


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


def write_psql_calls_to_file(release, sql):
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
        f.close()


def write_psql_calls_bydb_to_file(release, sql):
    envs = Environment.Env.get_envs(exclude=['mlff_test'])
    l = os.listdir(f'out/{release}/sql_bydb')
    for env in envs[0:]:
        print(env)
        baseport = Environment.Env._env_ports[env]
        passw = utils_sec.password_from_file('postgres', baseport)
        for dbname in [x.replace('.sql','') for x in l]:
            f = open(f'out/{release}/{env}/run_psql_{dbname}.bat', 'w')
            f.write(f'@SET PGPASSWORD={passw}\n')
            domain = Environment.Env.get_domain_from_dbname(dbname)
            offset = Environment.Env._domain_offsets[domain]
            if env == 'local':
                passw = 'postgres'
                baseport = 5432
                offset = 0
            f.write(f'psql -p {(baseport + offset)} -U postgres -d postgres -a -f ../sql_bydb/{dbname}.sql >{dbname}.out \n')
            f.close()


if __name__ == '__main__':
    gen_plsql_scripts()
