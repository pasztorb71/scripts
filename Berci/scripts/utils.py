import os
from inspect import getfile

import psycopg2
from tabulate import tabulate

from Cluster import Cluster
from docker_ips import new_base, offset, base_ips
from utils_db_schema import get_sema_from_dbname
from utils_repo import get_instance_from_repo_full_name


def move_upper_dir(path):
    return path.rsplit('/',1)[0] if path[-1] != '/' else path.rsplit('/',2)[0]


def git_init(base):
    os.system('git -C '+base+' restore --staged etc/release/release.sh')
    os.system('git -C '+base+' restore .')
    os.system('git -C '+base+' clean -f -d')

def git_init_from_path(path):
    a = path.split('\\', 2)
    repo = a[0] + '/' + a[1]
    git_init(repo)

def has_header(l):
    return isinstance([0], list)


def print_sql_result(d, maxlength, header=False):
    for db, records in sorted(d.items()):
        print(f"{db}:".ljust(maxlength))
        if records:
            if isinstance(records, str):
                print(f"  {records}")
            else:
                if header and has_header(records):
                    print(tabulate(records[1:], headers=records[0], tablefmt="pipe"))
                    print()
                else:
                    #print(f"records: {records}")
                    for value in records:
                        print('  ' + value)
    print(f'Összesen: {len(d)} db repo')

def get_port(env, repo_full_name=''):
    if env == 'sandbox':
        return 5433
    elif env == 'dev':
        return 5434
    elif env == 'fit':
        return 5435
    elif env == 'perf':
        return 5436
    elif env == 'cantas_train':
        return 5437
    elif env == 'cantas_test':
        return 5438
    elif env == 'local':
        return 5432
    elif env.startswith('new_'):
        inst = get_instance_from_repo_full_name(repo_full_name)
        return new_base[env] + offset[inst]


def get_env(port):
    if port == 5433:
        return 'sandbox'
    elif port == 5434:
        return 'dev'
    elif port == 5435:
        return 'fit'
    elif port == 5436:
        return 'perf'
    elif port == 5437:
        return 'cantas_train'
    elif port == 5438:
        return 'cantas_test'
    elif port == 5432:
        return 'local'

def get_password(env, user):
    if user != 'postgres':
        return 'mlffTitkosPassword123!'
    return 'fLXyFS0RpmIX9uxGII4N' if env != 'local' else 'mysecretpassword'


def password_from_file(puser, phost, pport):
    pass_out = ''
    with open(getfile(password_from_file).rsplit('\\',1)[0] + '/db_passw.txt', 'r') as f:
        for line in f.read().split('\n'):
            if line.startswith('#'):
                continue
            user, host, port, passw = line.split()
            if '_service' in puser and '_service' in user:
                pass_out = passw
                break
            if host == phost and port == str(pport) and user == puser:
                pass_out = passw
                break
    return pass_out


def get_login_from_file():
    with open(getfile(get_login_from_file).rsplit('\\',1)[0] + '/icell_passw.txt', 'r') as f:
        return f.read().split()


def has_history_table(db, schema, table):
    conn = get_conn('local', db, 'postgres')
    cur = conn.cursor()
    cur.execute("select count(*) from pg_tables where schemaname = '" + schema + "' and tablename = '" + table + "$hist'")
    res = cur.fetchone()[0]
    return res == 1


def get_conn(env, db, user):
    port = get_port(env)
    p = password_from_file(user, 'localhost', port)
    try:
        return psycopg2.connect(
            host='localhost',
            port=port,
            database=db,
            user=user,
            password=password_from_file(user, 'localhost', port))
    except Exception as e:
        print(e)


def get_all_databases(env):
    host, port = 'localhost', get_port(env)
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    return cluster.databases

def whoami(  ):
    import sys
    return f'--- {sys._getframe(1).f_code.co_name} ---'


def repo_in_newloc(repo, loc):
    repos = """
    """


def get_ip_address_for_docker(repo, loc):
    #oc = 'new_'+loc if repo_in_newloc(repo, loc) else loc
    if loc.startswith('new_'):
        inst = get_instance_from_repo_full_name(repo)
        return 'gateway.docker.internal:' + str(new_base[loc] + offset[inst])
    else:
        return base_ips[loc]


def print_table_level_check(return_dict, filtered=False):
    for db, data in sorted(return_dict.items()):
        if not data:
            continue
        if not filtered:
            print(db)
            maxlength = len(max([list(x.keys())[0] for x in data], key=len)) + 5
            for tabledict in data:
                key = list(tabledict.keys())[0]
                print(f'  {key.ljust(maxlength + 2)}{tabledict[key]}')
            continue
        tables_not_ok = [list(x.keys())[0] for x in data if list(x.values())[0] == 'NOT OK']
        if tables_not_ok:
            print(db)
            maxlength = len(max(tables_not_ok, key=len)) + 2
            for table in tables_not_ok:
                print(f'  {table.ljust(maxlength + 2)}NOT OK')


def get_conn_service_user(env, db):
    port = get_port(env)
    try:
        return psycopg2.connect(
            host='localhost',
            port=port,
            database=db,
            user=get_sema_from_dbname(db) + '_service',
            password='mlffTitkosPassword123!')
    except:
        return None


