import os
import re
import shutil
from distutils.dir_util import copy_tree
from inspect import getfile
from os.path import exists

import psycopg2
from tabulate import tabulate

from Cluster import Cluster
from docker_ips import new_base, offset, base_ips


def move_upper_dir(path):
    return path.rsplit('/',1)[0] if path[-1] != '/' else path.rsplit('/',2)[0]


def move_file(src, dst):
    print('file: '+src, dst)
    if os.path.isfile(src):
        print('  '+src)
        shutil.move(src, dst)


def copy_file(src, dst):
    print('file: '+src, dst)
    if os.path.isfile(src):
        print('  '+src)
        shutil.copyfile(src, dst)
    else:
        print('  '+ src + '  nem létezik')


def copy_file_and_replace(src, dst, from_to):
    copy_file(src, dst)
    replace_in_file(dst, from_to)


def move_dir(src, dst):
    print('dir : '+src, dst)
    if os.path.isdir(src):
        print('  '+src)
        shutil.move(src, dst)


def copy_dir(src, dst, delete_dir_if_exists=False):
    print('dir : '+src, dst)
    if delete_dir_if_exists == False and os.path.isdir(dst):
        raise Exception('Directory már létezik: ' + dst)
    if os.path.isdir(src):
        print('  '+dst)
        copy_tree(src, dst)


def create_old_file(fname):
    if os.path.isfile(fname + '_old'):
        raise Exception('már létezik: ' + fname + '_old')
        # os.remove(fname)
        # move_file(fname + '_old', fname)
    move_file(fname, fname + '_old')


def replace_in_file(fname, from_to):
    text = ''
    with open(fname, 'r', encoding='utf-8') as f:
        text = f.read()
        for pair in from_to:
            text = text.replace(pair[0], pair[1])
            text = text.replace(pair[0].upper(), pair[1].upper())
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(text)


def get_db_name(base):
    m = re.match('.*mlff-(.*)-postgredb', base)
    if m:
        return m.group(1)
    if 'doc-postgredb' in base:
        return 'document'


def get_schema(base, db_path):
    line = ''
    pattern = '.*property name="schema_name.*value="(.*)"/>'
    p = base+db_path+'/' + get_sema_from_dbname(db_path)
    with open(base+db_path+'/' + get_sema_from_dbname(db_path) + '/liquibase-install-schema.xml', 'r', encoding='utf-8') as f:
        text = f.read().splitlines()
        for l in text:
            m = re.match(pattern, l)
            if m:
                return m.group(1)
    return ''


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


def get_tablename_from_command(repo, command):
    command = command.replace('IF EXISTS ','').replace('"','')
    if command.startswith('DROP INDEX '):
        return repo.get_tablename_from_indexname(command.replace('DROP INDEX ', '').replace(';', ''))
    patterns = ["ALTER TABLE (\w+[.])?([a-zA-z0-9_$\"]+)",
                "COMMENT ON COLUMN (\w+[.])?([a-zA-z0-9_$\"]+)",
                "CREATE.*INDEX .* ON (\w+)[.]?([a-zA-z0-9_$\"]+)",
                "UPDATE (\w+[.])?([a-zA-z0-9_\"]+)",
                "DELETE FROM (\w+[.])?([a-zA-z0-9_\"]+)",
                "GRANT .* ON TABLE (\${.*}).(.*) TO ",
                ".* TABLE (\w+[.])?([a-zA-z0-9_$\"]+)",
                "INSERT INTO (\w+[.])?([a-zA-z0-9_\"]+)",
                ]
    outs = [re.match(pattern, command) for pattern in patterns]
    try:
        m = next(item for item in outs if item is not None)
    except:
        m = None
    if outs[2]:                     # CREATE.*INDEX
        return m.group(2)
    return m.group(2).replace('"','') if m else ''


def get_columnname_from_command(command):
    command = command.replace('IF EXISTS ','').replace('"','')
    m = None
    if 'DROP COLUMN ' in command:
        m = re.match(".* DROP COLUMN (\w+)", command)
    elif ' COLUMN ' in command:
        m = re.match(".* COLUMN ([a-zA-z0-9._\"$]+) ", command)
    elif ' ADD ' in command and 'CONSTRAINT' not in command:
        m = re.match(".* ADD ([a-zA-z0-9._\"]+) ", command)
    elif ' ADD CONSTRAINT' in command:
        m = re.match(".* CHECK \(\(\((\w+)", command)
    elif 'UPDATE ' in command:
        m = re.match("UPDATE .* SET (\w+)", command)
    return m.group(1).split('.')[-1].replace('"','') if m else ''

def get_schema_from_command(command):
    command = command.replace('IF EXISTS ','').replace('"','')
    patterns = ["ALTER SCHEMA ([a-zA-z0-9_\"]+) ",
                "ALTER TABLE ([a-zA-z0-9_\"]+)",
                "COMMENT ON COLUMN ([a-zA-z0-9_\"]+)",
                ".* INDEX .* (?:ON )([a-zA-z0-9_\"]+)",
                "UPDATE ([a-zA-z0-9_\"]+)",
                "DELETE FROM ([a-zA-z0-9_\"]+)",
                "DROP INDEX (.*)\.",
                "GRANT .* ON TABLE \${schema_name_(\w+)",
                ".* TABLE ([a-zA-z0-9_\"]+)",
                ".*TRIGGER .*ON \${schema_name_(\w+)",
                "ALTER INDEX (\w+)"]
    outs = [re.match(pattern, command) for pattern in patterns]
    try:
        m = next(item for item in outs if item is not None)
    except:
        m = None
    return m.group(1).replace('"','') if m else ''


def get_consname_from_command(command):
    command = command.replace('IF EXISTS ', '').replace('"', '')
    m = re.match(".*CONSTRAINT (\w+)[;]?", command)
    return m.group(1) if m else ''


def get_indexname_from_command(command):
    command = command.replace('IF EXISTS ', '').replace('"', '')
    patterns = ["DROP INDEX .*\.(\w+)",
                "ALTER INDEX .*\.(\w+) RENAME TO \w+",
                ".* INDEX (\w+)[;]?",]
    outs = [re.match(pattern, command) for pattern in patterns]
    try:
        m = next(item for item in outs if item is not None)
    except:
        m = None
    return m.group(1)  if m else ''


def get_triggername_from_command(command):
    m = re.match(".*TRIGGER (?:IF EXISTS) ([a-zA-z0-9_$\"]+)[;]?", command)
    return m.group(1)  if m else ''


def get_files_from_path_ext_filtered(path, ext, cont):
    out = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext) and cont in file:
                out.append(os.path.join(root, file))
    return out

def get_files_from_path_fname_filtered(path, name):
    out = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file:
                out.append(os.path.join(root, file))
    return out

def get_files_from_path_ext_find_content(path, ext, cont):
    out = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                if file_contains(os.path.join(root, file), cont):
                    out.append(os.path.join(root, file))
    return out


def file_contains(file, cont,):
    with open(file, 'r', encoding='utf-8') as f:
        if cont in f.read():
            return True
    return False


def get_repo_from_schema(schema):
    r = ''
    base = 'c:/GIT/MLFF/'
    for repo in os.listdir(base):
        path = base + repo + '/liquibase/'
        dbname = os.listdir(path)
        path += dbname[0]
        schem = filter(lambda file: os.path.isdir(path+'/'+file), os.listdir(path))
        s = [dir for dir in list(schem) if dir not in ('_init_dbs', 'all-modules')]
        if s[0] == schema:
            r = repo
            break
    return r


def load_from_file(fname):
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open('/'.join([project_root,'scripts',fname]), 'r') as f:
        return [x for x in f.read().split('\n') if not x.startswith('#')]

def get_last_nth_occurence_of_list_element(plist, pelem, nth):
    index_after = [idx for idx, s in enumerate(plist) if pelem in s]
    if not index_after:
        return None
    return index_after[-nth] + 1

def append_to_file_after_line_last_occurence(fname, after, what):
  with open(fname, 'r', encoding='utf-8') as f:
    text = f.readlines()
  already_exists = [idx for idx, s in enumerate(text) if what in s]
  if already_exists:
    return
  index_after = get_last_nth_occurence_of_list_element(text, after, 1)
  if not index_after:
      index_header_end = get_last_nth_occurence_of_list_element(text, '    <!-- ==================================', 2)
      if not index_header_end:
        return
      else:
          index_after = index_header_end + 1
  text.insert(index_after, what + '\n')
  with open(fname, 'w', encoding='utf-8') as out:
    out.write(''.join(text))

def get_dbname_from_project(project):
    db = get_db_name(project)
    return db.replace('-', '_')


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


def format_sql(pre):
    return pre.replace(' WHERE ', '\n   WHERE ').replace(' AND ', '\n     AND ')


def get_all_databases(env):
    host, port = 'localhost', get_port(env)
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    return cluster.databases

def whoami(  ):
    import sys
    return f'--- {sys._getframe(1).f_code.co_name} ---'

def get_instance_from_repo_full_name(repo):
    if repo == 'doc-postgredb':
        return 'pg-doc-mqid'
    else:
        id = repo.split('-')[1]
        return 'pg-' + id + '-mqid'

def get_ip_addresses_for_docker(repo, loc):
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


def get_sema_from_dbname(db):
    if db == 'document':
        return 'document_meta'
    if db == 'payment_transaction':
        return 'payment_transaction'
    return db.split('_', 1)[1]