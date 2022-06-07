import pprint
from inspect import getfile

from tabulate import tabulate


def print_dict(d):
    for db, records in sorted(d.items()):
        print(db + ': ', end='')
        print(d[db])

def print_dict_queried(d):
    for db, records in d.items():
        print(db)
        if records:
            print(tabulate(records[1:], headers=records[0], tablefmt="pipe"))

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


def get_sema(db):
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