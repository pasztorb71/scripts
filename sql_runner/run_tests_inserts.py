import re

import psycopg2

from Cluster import Cluster
from cmdlist import cmdlist
from utils import password_from_file, get_sema_from_dbname, get_port


def get_conn(env, db):
    port = get_port(env)
    return psycopg2.connect(
        host='localhost',
        port=port,
        database=db,
        user=get_sema_from_dbname(db) + '_service',
        password='mlffTitkosPassword123!')


def runteszt(conn):
    print(conn.info.dbname)
    cmd_list = cmdlist[conn.info.dbname]
    if not cmd_list:
        return
    cur = conn.cursor()
    for cmd in cmd_list:
        short_cmd = re.match("(\w+\s+\w+\s+\w+)", cmd, flags=re.DOTALL|re.MULTILINE).group(1)
        print('  ' + short_cmd, end='')
        try:
            cur.execute(cmd)
            print(': OK')
        except Exception as e:
            print(': ' + str(e).split('\n')[0])
            conn.rollback()
    conn.commit()

def cmddiff(env):
    cluster = Cluster('localhost', '5433', 'fLXyFS0RpmIX9uxGII4N')
    dbdatabases = cluster.databases
    cmdlistdbs = [db for db in cmdlist][0]
    return set(dbdatabases) - set(cmdlistdbs)


if __name__ == '__main__':
    host, port = 'localhost', 5433
    cluster = Cluster(host=host, port=port, passw=password_from_file(host, port))
    #databases = load_from_file('../databases.txt')
    databases = ['payment_account_info']
    #databases = cluster.databases
    for db in databases:
        runteszt(get_conn('local',db))
    exit(0)
    runteszt(get_conn('sandbox','core_template'))
    runteszt(get_conn('sandbox','core_customer'))
    runteszt(get_conn('sandbox','enforcement_visual_check'))
