import os
import subprocess

import Repository

from Git.Git_class import Git
from Git.utils_parallel_runner import parallel_run, _mproc_multiple_commands
import utils


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
            utils.print_sql_result(ret_dict, 52)
            if input("Mehet a frissítés? [y/n]") == "y":
                synchronize_branch_in_multiple_repos(gitlist, branch='master')
            else:
                break
        else:
            print('Nincsen differencia')
            break


def delete_branch_multiple_repos(gitlist, branch):
    commands = [f'branch -d {branch}' ]
    ret_dict = parallel_run(gitlist, _mproc_multiple_commands, commands)


def create_branch_multiple_repos(gitlist, branch):
    commands = ['checkout -b ' + branch]
    ret_dict = parallel_run(gitlist, _mproc_multiple_commands, commands)

def create_stage_and_commit(gitlist, message):
    commands = [f'commit -a -m "{message}"' ]
    ret_dict = parallel_run(gitlist, _mproc_multiple_commands, commands)


def push_branch(gitlist, branch):
    commands = [f'push origin {branch}' ]
    ret_dict = parallel_run(gitlist, _mproc_multiple_commands, commands)


if __name__ == '__main__':
    repo = Repository.Repository()
    base = repo.get_base()
    repo_names = repo.get_repo_names()
    #gitlist = [Git(base, name) for name in repo_names if name != 'doc-postgredb'][0:]
    gitlist = Git.get_gitlist()
    check_diff_and_synchronize()
    exit(0)
    #synchronize_branch_in_multiple_repos(gitlist, branch='master')
    #create_branch_multiple_repos(gitlist, 'feature/MLFFDEV-15855-liquibase-hez-a-service-user-jelszava-erkezzen-kornyezeti-valtozoban')
    #create_stage_and_commit(gitlist, 'MLFFDEV-15855  rollback')
    #push_branch(gitlist, 'feature/MLFFDEV-15855-liquibase-hez-a-service-user-jelszava-erkezzen-kornyezeti-valtozoban')
    delete_branch_multiple_repos(gitlist, 'feature/MLFFDEV-15855-liquibase-hez-a-service-user-jelszava-erkezzen-kornyezeti-valtozoban')
