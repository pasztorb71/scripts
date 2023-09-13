from inspect import getfile

from tabulate import tabulate

import Repository
from Cluster import Cluster
import Environment
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


def get_instance_from_db_name(dbname):
    if dbname == 'document':
        return 'pg-doc'
    return 'pg-' + dbname.split('_')[0]


def get_atlassian_login_from_file():
    with open(getfile(get_atlassian_login_from_file).rsplit('\\', 1)[0] + '/icell_passw.txt', 'r') as f:
        return f.read().split()


def whoami(  ):
    import sys
    return f'--- {sys._getframe(1).f_code.co_name} ---'


def get_ip_address_for_docker(repo, loc):
    if loc == 'local':
        return 'gateway.docker.internal'
    elif loc == 'mlff_test':
        return 'gateway.docker.internal:5555'
    elif loc == 'anonymizer-test':
        return 'gateway.docker.internal:5556'
    inst = Repository.get_instance_from_repo_full_name(repo)
    return 'gateway.docker.internal:' + str(Environment.Env.new_base[loc] + Environment.Env.offset[inst])


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


def get_cluster_databases(env, port=''):
    if not port:
        port = Environment.Env(env).get_port_from_repo()
    host = 'localhost'
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', port))
    return cluster.databases[0:]


def get_last_nth_occurence_of_list_element(plist, pelem, nth):
    index_after = [idx for idx, s in enumerate(plist) if pelem in s]
    if not index_after:
        return None
    return index_after[-nth] + 1

