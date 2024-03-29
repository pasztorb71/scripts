import re

from Cluster import Cluster
from checks.cmdlist import cmdlist
from sql_runner.parallel_runner.multiprocess import parallel_run_multiprocess
from utils.utils import print_sql_result
from Environment import get_conn_service_user
from utils.utils_sec import password_from_file


def runteszt(host, port, db, return_dict):
    conn = get_conn_service_user('local', db)
    cmd_list = []
    try:
        cmd_list = cmdlist[conn.info.dbname]
    except KeyError:
        print(f"{conn.info.dbname} : no commands")
    #except AttributeError:
    #    print('AttributeError: ' + db)
    if not cmd_list:
        return
    out = []
    cur = conn.cursor()
    for cmd in cmd_list:
        short_cmd = re.match("(\w+\s+\w+\s+\w+)", cmd, flags=re.DOTALL|re.MULTILINE).group(1)
        try:
            cur.execute(cmd)
            out.append(short_cmd + ': OK')
        except Exception as e:
            out.append(short_cmd + ': ' + str(e).split('\n')[0])
            conn.rollback()
    conn.commit()
    return_dict[db] = out

def cmddiff(env):
    cluster = Cluster('localhost', '5433', 'fLXyFS0RpmIX9uxGII4N')
    dbdatabases = cluster.databases
    cmdlistdbs = [db for db in cmdlist][0]
    return set(dbdatabases) - set(cmdlistdbs)


if __name__ == '__main__':
    host, port = 'localhost', 5442
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    #databases = load_from_file('../databases.txt')
    databases = ['enforcement_detection']
    #databases = cluster.databases
    return_dict = parallel_run_multiprocess(host, [port], databases, runteszt)
    print_sql_result(return_dict,50, header=False)

