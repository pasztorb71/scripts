from inspect import getfile

import psycopg2
from tabulate import tabulate

from Cluster import Cluster
from docker_ips import new_base, offset
import utils_db
import utils_repo
from utils_sec import password_from_file


def move_upper_dir(path):
    return path.rsplit('/',1)[0] if path[-1] != '/' else path.rsplit('/',2)[0]


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

def print_one_result(d, maxlength):
    for db, value in sorted(d.items()):
        print(f"{db}:".ljust(maxlength), end='')
        if value:
            print(value)
        else:
            print()

def get_old_port(env, repo_full_name=''):
    if env == 'sandbox':
        return 5433
    elif env == 'dev':
        return 5434
    elif env == 'fit':
        return 5435
    elif env == 'perf':
        return 5436
    elif env == 'train':
        return 5437
    elif env == 'test':
        return 5438
    elif env == 'cron_test':
        return 5555
    elif env == 'local':
        return 5432
    else:
        print(f"utils.get_port('{env}')\n" + """"Nem létező környezet:
Lehetséges értékek:
  sandbox
  dev
  fit
  perf
  train
  test
  new_""")
        raise Exception("Nem létező környezet")

def get_port(env, repo_full_name):
    if env == 'local':
        return 5432
    elif env == 'mlff-test':
        return 5555
    elif env == 'anonymizer-test':
        return 5556
    inst = utils_repo.get_instance_from_repo_full_name(repo_full_name)
    return new_base[env] + offset[inst]

def get_ports_from_env(env) -> list[int]:
    if env == 'local':
        return [5432]
    ports = []
    for idx in offset.values():
        ports.append(new_base[env] + idx)
    return ports


def get_env_old(port):
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

def get_env(port):
    prevkey = ''
    for env, p in new_base.items():
        if port < p:
            return prevkey
        prevkey = env
    return None

def get_instance_from_db_name(dbname):
    if dbname == 'document':
        return 'pg-doc'
    return 'pg-' + dbname.split('_')[0]

def get_port_from_env_inst(env, inst):
    if env in new_base:
        if inst in offset:
            return new_base[env] + offset[inst]
        else:
            print("Lehetséges instance-ok:")
            print('\n'.join([x for x in offset.keys()]))
            raise Exception("Nem létező instance")
    else:
        print(f"utils.get_port_from_env_inst('{env}')\n" + """"Nem létező környezet:
    Lehetséges értékek:
      sandbox
      dev
      fit
      perf
      train
      test
      new_""")
        raise Exception("Nem létező környezet")


def get_password(env, user):
    if user != 'postgres':
        return 'mlffTitkosPassword123!'
    return 'fLXyFS0RpmIX9uxGII4N' if env != 'local' else 'mysecretpassword'


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
    port = get_port(env, utils_db.get_repository_name_from_dbname(db))
    p = password_from_file(user, port)
    try:
        return psycopg2.connect(
            host='localhost',
            port=port,
            database=db,
            user=user,
            password=password_from_file(user, port))
    except Exception as e:
        print(e)


def get_all_databases(env):
    host, port = 'localhost', get_port(env)
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    return cluster.databases

def whoami(  ):
    import sys
    return f'--- {sys._getframe(1).f_code.co_name} ---'


def get_ip_address_for_docker(repo, loc):
    if loc == 'local':
        return 'gateway.docker.internal'
    elif loc == 'mlff-test':
        return 'gateway.docker.internal:5555'
    elif loc == 'anonymizer-test':
        return 'gateway.docker.internal:5556'
    inst = utils_repo.get_instance_from_repo_full_name(repo)
    return 'gateway.docker.internal:' + str(new_base[loc] + offset[inst])


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
    port = get_port(env, utils_db.get_repository_name_from_dbname(db))
    try:
        return psycopg2.connect(
            host='localhost',
            port=port,
            database=db,
            user=utils_db.get_sema_from_dbname(db) + '_service',
            password='mlffTitkosPassword123!')
    except:
        return None


def get_cluster_databases(env, port=''):
    if not port:
        port = get_port(env)
    host = 'localhost'
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', port))
    return cluster.databases[0:]


def get_last_nth_occurence_of_list_element(plist, pelem, nth):
    index_after = [idx for idx, s in enumerate(plist) if pelem in s]
    if not index_after:
        return None
    return index_after[-nth] + 1

def get_envs(exclude=['']) -> list[str]:
    return [env for env in new_base if env not in exclude]
