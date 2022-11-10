import os
import re


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


def get_dbname_from_project(project):
    db = get_db_name(project)
    return db.replace('-', '_')


def get_sema_from_dbname(db):
    if db == 'document':
        return 'document_meta'
    if db == 'payment_transaction':
        return 'payment_transaction'
    return db.split('_', 1)[1]