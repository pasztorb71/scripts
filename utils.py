import os
import re
import shutil
from inspect import getfile
from tabulate import tabulate

from setuptools._distutils.dir_util import copy_tree


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


def copy_file_and_replace(src, dst, from_to):
    copy_file(src, dst)
    replace_in_file(dst, from_to)


def move_dir(src, dst):
    print('dir : '+src, dst)
    if os.path.isdir(src):
        print('  '+src)
        shutil.move(src, dst)


def copy_dir(src, dst):
    print('dir : '+src, dst)
    if os.path.isdir(dst):
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
    with open(base+db_path+'/_init_dbs/' + db_path + '-db-install.xml', 'r', encoding='utf-8') as f:
        text = f.read()
    return re.match('.*property name="schema_name_.*value="(.*)"/>', text, flags=re.DOTALL|re.MULTILINE).group(1)


def git_init(base):
    os.system('git -C '+base+' restore --staged etc/release/release.sh')
    os.system('git -C '+base+' restore .')
    os.system('git -C '+base+' clean -f -d')


def print_dict(d):
    for db, records in sorted(d.items()):
        print(db + ': ', end='')
        print(d[db])

def print_dict_queried(d):
    for db, records in d.items():
        print('Database: ' + db)
        if records:
            print(tabulate(records[1:], headers=records[0], tablefmt="pipe"))
        print()


def get_port(env):
    if env == 'sandbox':
        return 5433
    elif env == 'dev':
        return 5434
    elif env == 'fit':
        return 5435
    elif env == 'local':
        return 5432


def get_password(env, user):
    if user != 'postgres':
        return 'mlffTitkosPassword123!'
    return 'fLXyFS0RpmIX9uxGII4N' if env != 'local' else 'mysecretpassword'


def get_sema_from_dbname(db):
    if db == 'document':
        return 'document_meta'
    if db == 'payment_transaction':
        return 'payment_transaction'
    return db.split('_', 1)[1]


def password_from_file(phost, pport):
    with open(getfile(password_from_file).rsplit('\\',1)[0] + '/params.txt', 'r') as f:
        for line in f.read().split('\n')[1:]:
            host, port, passw = line.split()
            if host == phost and port == pport:
                break
    return passw


def get_tablename_from_command(command):
    command = command.replace('IF EXISTS ','').replace('"','')
    patterns = ["ALTER TABLE (\w+[.])?([a-zA-z0-9_$\"]+)",
                "COMMENT ON COLUMN (\w+[.])?([a-zA-z0-9_$\"]+)",
                "CREATE INDEX .* ON (\w+[.])?([a-zA-z0-9_$\"]+)",
                "UPDATE (\w+[.])?([a-zA-z0-9_\"]+)",
                "GRANT .* ON TABLE (\${.*}).(.*) TO ",
                ".* TABLE (\w+[.])?([a-zA-z0-9_$\"]+)",
                ]
    outs = [re.match(pattern, command) for pattern in patterns]
    try:
        m = next(item for item in outs if item is not None)
    except:
        m = None
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
    patterns = ["ALTER TABLE ([a-zA-z0-9_\"]+)",
                "COMMENT ON COLUMN ([a-zA-z0-9_\"]+)",
                ".* INDEX .* (?:ON )([a-zA-z0-9_\"]+)",
                "UPDATE ([a-zA-z0-9_\"]+)",
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
                "ALTER INDEX .*RENAME TO (\w+)",
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