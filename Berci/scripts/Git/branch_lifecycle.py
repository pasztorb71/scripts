import Repository

from Git.Git_class import Git
from Git.services import create_stage_and_commit, push_branch, delete_branch_multiple_repos, \
    create_branch_multiple_repos

if __name__ == '__main__':
    #gitlist = Git.get_gitlist(exclude=[''])
    gitlist = Git.get_gitlist(exclude=['empty'])[1:]
    branch = 'feature/MLFFSUP-6252_New_version_of_-_Source_system_ddl_change_tracker'
    #create_branch_multiple_repos(gitlist, branch)
    #create_stage_and_commit(gitlist, 'MLFFSUP-6252  New_version_of_-_Source_system_ddl_change_tracker')
    #push_branch(gitlist, branch)
    delete_branch_multiple_repos(gitlist, branch)
