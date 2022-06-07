import collections
import multiprocessing
import os
import subprocess

from Git.Git_class import Git
from sql_runner.utils import print_dict


def _mproc_ck_branch(git, return_dict, branch):
    os.popen('git -C '+git.base+'/'+git.repo+' fetch --all --prune').read()
    proc=subprocess.Popen('cmd /u /c git -C ' + git.base +'/' + git.repo +' diff '+branch+' origin/'+branch, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    res = proc.stdout.read().decode('utf-8')
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


def is_all_branches_synchronized(gitlist, branch):
    ret_dict =  parallel_run(gitlist, _mproc_ck_branch, branch)
    #filtered = {repo: status for repo, status in ret_dict.items() if status != 'OK'}
    print_dict(ret_dict)


def synchronize_all_master_branch(gitlist):
    commands = ['checkout master', 'pull origin master']
    return parallel_run(gitlist, _mproc_multiple_commands, commands)


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    repos = os.listdir(base)[0:]
    #repos = ['mlff-core-notification-wa-postgredb']
    gitlist = [Git(base, repo) for repo in repos]
    synchronize_all_master_branch(gitlist)
    is_all_branches_synchronized(gitlist, 'master')

