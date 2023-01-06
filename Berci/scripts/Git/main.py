import multiprocessing
import os
import subprocess

import Repository

from Git.Git_class import Git
from Ticket import Ticket
from utils import print_sql_result


def _mproc_ck_branch(git, return_dict, branch):
    os.system('git -C '+git.base+'/'+git.repo+' fetch --all --prune')
    proc=subprocess.Popen('cmd /u /c git -C ' + git.base +'/' + git.repo +' diff '+branch+' origin/'+branch,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = proc.stdout.read()
    git.synced = 'OK' if not res else 'Remote is ahead'
    if git.synced == 'OK':
        proc = subprocess.Popen('cmd /u /c git -C ' + git.base + '/' + git.repo + ' status --porcelain',
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = proc.stdout.read()
        if res:
            git.synced = 'Local commits ahead'

    proc.kill()
    return_dict[git.repo] = git.synced

def _mproc_multiple_commands(git, return_dict, commands):
    out = []
    err = []
    for cmd in commands:
        proc=subprocess.Popen('cmd /u /c git -C ' + git.base +'/' + git.repo +' '+cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out.append(proc.stdout.read().decode('utf-8'))
        e = proc.stderr.read().decode('utf-8')
        if any(x in e for x in ['error:', 'Aborting']):
            err.append(e)
    return_dict[git.repo] = {'stdout': out, 'stderr': err}


def wait_until_end(jobs):
    for job in jobs:
        job.join()


def get_return_dict():
    manager = multiprocessing.Manager()
    return manager.dict()


def parallel_run(gitlist, proc_to_run, *args):
    return_dict = get_return_dict()
    jobs = []
    for git in gitlist:
        p = multiprocessing.Process(target=proc_to_run, args=(git, return_dict, *args))
        jobs.append(p)
        p.start()
    wait_until_end(jobs)
    return return_dict


def is_branch_synchronized_in_multiple_repos(gitlist, branch, filtered='n'):
    ret_dict = parallel_run(gitlist, _mproc_ck_branch, branch)
    if filtered == 'y':
        return {repo: status for repo, status in ret_dict.items() if status != 'OK'}
    return ret_dict

def synchronize_branch_in_multiple_repos(gitlist, branch):
    commands = ['checkout '+branch, 'pull origin '+branch]
    ret_dict = parallel_run(gitlist, _mproc_multiple_commands, commands)
    for d in ret_dict:
        print(f"{d} : ", end='')
        if ret_dict[d]['stderr']:
            for i in ret_dict[d]['stderr']:
                print('\n  ' + i.replace('\n', '\n  '))
        else:
            print('Synchronizing ok')
    print('Synchronize_branch lefutott')


def create_branch(git, ticket):
    is_synced = git.is_master_synced()
    while not is_synced:
        print('A lokális master ág le van maradva')
        if input("Mehet a frissítés? [y/n]") == "y":
            git._run_command('checkout master')
            git._run_command('pull origin master')
            is_synced = git.is_master_synced()
        else:
            return
    git.checkout_branch('master')
    git.new_branch('feature/'+ticket.name+'_'+ticket.get_title())


def check_diff_and_synchronize():
    while True:
        ret_dict = is_branch_synchronized_in_multiple_repos(gitlist, branch='master', filtered='y')
        if ret_dict:
            print('Differencia:')
            print_sql_result(ret_dict, 52)
            if input("Mehet a frissítés? [y/n]") == "y":
                synchronize_branch_in_multiple_repos(gitlist, branch='master')
            else:
                break
        else:
            print('Nincsen differencia')
            break


def create_branch_multiple_repos(gitlist, branch):
    commands = ['checkout -b ' + branch]
    ret_dict = parallel_run(gitlist, _mproc_multiple_commands, commands)


if __name__ == '__main__':
    repo = Repository.Repository()
    base = repo.get_base()
    repo_names = repo.get_repo_names()
    #repo_names = ['mlff-core-customer-postgredb', 'mlff-payment-invoice-postgredb']
    gitlist = [Git(base, name) for name in repo_names if name != 'mlff-data-ingestion-meta-postgredb'][0:]
    check_diff_and_synchronize()
    #synchronize_branch_in_multiple_repos(gitlist, branch='master')
    exit(0)
    create_branch_multiple_repos(gitlist, 'feature/MLFFDEV-9830-dwh_stream-user-letrehozasa-a-forras-db-kben-v2')