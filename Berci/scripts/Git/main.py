import multiprocessing
import os
import subprocess

from Repository import Repository

from Git.Git_class import Git
from utils import print_dict


def _mproc_ck_branch(git, return_dict, branch):
    os.popen('git -C '+git.base+'/'+git.repo+' fetch --all --prune')
    proc=subprocess.Popen('cmd /u /c git -C ' + git.base +'/' + git.repo +' diff '+branch+' origin/'+branch, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = proc.stdout.read()
    git.synced = 'OK' if not res else 'DIFF'
    return_dict[git.repo] = 'OK' if not res else 'DIFF'

def _mproc_multiple_commands(git, return_dict, commands):
    out = []
    for cmd in commands:
        proc=subprocess.Popen('cmd /u /c git -C ' + git.base +'/' + git.repo +' '+cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out.append(proc.stdout.read().decode('utf-8'))
    return_dict[git.repo] = out


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
    print('Synchronize_branch lefutott')
    return ret_dict


def create_branch(git, ticket):
    is_synced = git.is_master_synced()
    if not is_synced:
        print('A lokális master ág le van maradva')
        exit(1)
    else:
        git.checkout_branch('master')
        git.new_branch('feature/'+ticket.name+'_'+ticket.get_title())


if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repo_names = repo.get_repo_names()
    #repos = ['mlff-payment-psp-proxy-postgredb']
    gitlist = [Git(base, name) for name in repo_names]
    #create_branch(gitlist[0], Ticket('MLFFDEV-4498'))
    #synchronize_branch_in_multiple_repos(gitlist, branch='master')
    ret_dict = is_branch_synchronized_in_multiple_repos(gitlist, branch='master', filtered='y')
    print('Differencia:')
    print_dict(ret_dict)


