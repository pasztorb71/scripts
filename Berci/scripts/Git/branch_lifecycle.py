import Repository

from Git.Git_class import Git
from Git.services import create_stage_and_commit, push_branch, delete_branch_multiple_repos, \
    create_branch_multiple_repos

if __name__ == '__main__':
    #gitlist = Git.get_gitlist(exclude=[''])
    gitlist = Git.get_gitlist(exclude=['empty'])
    branch = 'feature/MLFFSUP-5392_Source_system_ddl_change_tracker_bug_fix_install'
    #create_branch_multiple_repos(gitlist, branch)
    #create_stage_and_commit(gitlist, 'MLFFSUP-5392  Source_system_ddl_change_tracker_bug_fix_install')
    #push_branch(gitlist, branch)
    delete_branch_multiple_repos(gitlist, branch)
