import Repository

from Git.Git_class import Git
from Git.services import create_stage_and_commit, push_branch, delete_branch_multiple_repos, \
    create_branch_multiple_repos

if __name__ == '__main__':
    gitlist = [git for git in Git.get_gitlist() if 'tariff' not in git.repo]
    #gitlist = Git.get_gitlist()
    branch = 'feature/MLFFSUP-4281_A_ddl_logoló_finomhangolása'
    #create_branch_multiple_repos(gitlist, branch)
    #create_stage_and_commit(gitlist, 'MLFFSUP-4281  A_ddl_logoló_finomhangolása')
    #push_branch(gitlist, branch)
    delete_branch_multiple_repos(gitlist, branch)
