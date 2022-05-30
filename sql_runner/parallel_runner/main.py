import multiprocessing
import os

import psycopg2

import utils
from Cluster import Cluster
from utils import print_dict, print_dict_queried


def mproc(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password='fLXyFS0RpmIX9uxGII4N')
    cur = conn.cursor()
    cur.execute("SELECT schemaname, tablename, tableowner FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public')")
    record = cur.fetchall()
    return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record
    cur.close()
    conn.commit()
    conn.close()

def mproc_multiple_commands(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password='fLXyFS0RpmIX9uxGII4N')
    cur = conn.cursor()
    recout = []
    cur.execute("SELECT schemaname, tablename FROM pg_tables WHERE tableowner NOT IN ('cloudsqladmin') AND schemaname NOT IN ('public')")
    record = cur.fetchall()
    for rec in record:
        cur.execute("select '" + rec[0] + '.' + rec[1] + "', count(*) from " + rec[0] + '.' + rec[1])
        header = [[desc[0].upper() for desc in cur.description]]
        record1 = cur.fetchall()
        recout = recout + record1
    return_dict[db] = header + recout if record else []

    cur.close()
    conn.commit()
    conn.close()

def mproc_revoke_rights(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password='fLXyFS0RpmIX9uxGII4N')
    cur = conn.cursor()
    recout = []
    cur.execute("SELECT schema_name FROM information_schema.schemata WHERE schema_owner = 'postgres';")
    record = cur.fetchall()
    for rec in record:
        cmd = "REVOKE " + rec[0] + "_tbl_own FROM " + rec[0] + "_full;"
        cur.execute(cmd)
    return_dict[db] = cmd

    cur.close()
    conn.commit()
    conn.close()


def start_process(target, host, port, db, return_dict):
    p = multiprocessing.Process(target=target, args=(host, port, db, return_dict))
    jobs.append(p)
    p.start()


def wait_until_end(jobs):
    for job in jobs:
        job.join()


def get_return_dict():
    manager = multiprocessing.Manager()
    return manager.dict()


if __name__ == '__main__':
    host, port = 'localhost', 5435
    cluster = Cluster(host=host, port=port, passw=utils.password_from_file(host, port))
    #databases = load_from_file('databases.txt')
    databases = cluster.databases[0:]
    #databases = ['core_customer']
    return_dict = get_return_dict()
    jobs = []
    for db in databases:
        start_process(mproc_revoke_rights, host, port, db, return_dict)
    wait_until_end(jobs)
    print_dict(return_dict)
    #print_dict_queried(return_dict)

