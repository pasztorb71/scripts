import logging

from Cluster import Cluster
from Repository import Repository
from utils import password_from_file, get_conn, get_sema_from_dbname


def runteszt(env, db, user, cmd_list):
    conn = get_conn(env, db, user)
    log('debug', 'user: ' + user)
    result = _run(cmd_list, conn)
    sema = user.rsplit('_',1)[0]
    sum_result = []
    for idx,i in enumerate(result):
        sum_result.append(cmd_list[idx][1] == i[1])
    if not all(sum_result):
        log('info', '  ' + sema + ': Hiba')
    else:
        log('info', '  ' + sema + ': Ok')
    conn.commit()
    conn.close()


def _run(cmd_list, conn):
    result = []
    cur = conn.cursor()
    for cmd in cmd_list:
        cmd = cmd[0]
        log('debug', ' ' * 4 + cmd, end='')
        sh.terminator = "\n"
        try:
            r = [cmd]
            cur.execute(cmd)
            log('debug', ': OK')
            r.append('OK')
            result.append(r)
        except Exception as e:
            r.append('ERR')
            result.append(r)
            log('debug', ': ' + str(e).split('\n')[0])
            conn.rollback()
            if not any(elem in str(e) for elem in ['permission denied', 'must be owner of table', 'already exists']):
                raise e

    return result

def log(level, message, end='\n'):
    sh.terminator = end
    if level == 'debug':
        logger.debug(message)
    elif level == 'info':
        logger.info(message)
    else:
        raise Exception("Invalid loglevel ('debug', 'info'")
        sh.terminator = "\n"
    sh.terminator = "\n"

def get_cre_table(sema, table):
    return [
        # "drop table " + sema + table,
        ["create table " + sema + table + " (x numeric)", 'OK'],
        ["ALTER TABLE " + sema + table + " OWNER TO " + sema + "_tbl_own", 'OK'],
        ["GRANT SELECT ON TABLE " + sema + table + " TO " + sema + "_sel", 'OK'],
        ["GRANT INSERT, UPDATE ON TABLE " + sema + table + " TO " + sema + "_mod", 'OK'],
        ["GRANT DELETE, TRUNCATE ON TABLE " + sema + table + " TO " + sema + "_del", 'OK']
    ]


def tabla_modositas_teszt(env, db):
    expected_result = 'ERR' if env in ['dev', 'fit'] else 'OK'
    print(db)
    sema = get_sema_from_dbname(db)
    table = '.ttt_proba'
    cre_table = get_cre_table(sema, table)
    runteszt(env=env, db=db, user='postgres', cmd_list=cre_table)
    runteszt(env=env, db=db, user=sema + '_service',
             cmd_list=[["alter table " + sema + table + " add column y numeric", expected_result]])
    runteszt(env=env, db=db, user='postgres', cmd_list=[["drop table if exists " + sema + table, 'OK']])


def tabla_letrehozas_teszt(env, db):
    logger.info(db)
    sema = get_sema_from_dbname(db)
    table = '.ttt_proba_create'
    _cmd_list = [
                ["create table " + sema + table + " (x numeric)",'ERR'],
                ["drop table if exists " + sema + table, 'OK']
                 ]
    runteszt(env=env, db=db, user=sema + '_service', cmd_list=_cmd_list)


def load_from_file(fname):
    with open(fname, 'r') as f:
        return f.read().split()


def init_logging(level):
    # create logger
    logger = logging.getLogger('mylogger')
    logger.setLevel(logging.DEBUG)

    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(level)

    # create formatter
    formatter = logging.Formatter('%(message)s')

    # add formatter to ch
    ch.setFormatter(formatter)

    # add ch to logger
    logger.addHandler(ch)
    return logger, ch


if __name__ == '__main__':
    logger, sh = init_logging(logging.INFO)
    host, port = 'localhost', 5432
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    #databases = load_from_file('databases.txt')
    databases = cluster.databases[0:]
    databases = ['core_notification_wa']
    for db in databases:
        tabla_letrehozas_teszt('train', db)
        tabla_modositas_teszt('train', db)
