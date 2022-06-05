import multiprocessing
import os

import psycopg2

def mproc(base, repo, return_dict):
    os.system('git -C '+base+' git fetch --all --prune')
#    return_dict[db] = [[desc[0].upper() for desc in cur.description]] + record

def start_process(target, base, repo, return_dict):
    p = multiprocessing.Process(target=target, args=(base, repo, return_dict))
    jobs.append(p)
    p.start()


def wait_until_end(jobs):
    for job in jobs:
        job.join()


def get_return_dict():
    manager = multiprocessing.Manager()
    return manager.dict()


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    repos = ['mlff-core-vehicle-postgredb']
    return_dict = get_return_dict()
    jobs = []
    for repo in repos:
        start_process(mproc, base, repo, return_dict)
    wait_until_end(jobs)
    print_dict(return_dict)
    #print_dict_queried(return_dict)

