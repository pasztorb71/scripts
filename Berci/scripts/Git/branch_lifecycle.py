import Repository

from Git.Git_class import Git
from Git.services import create_stage_and_commit, push_branch, delete_branch_multiple_repos

if __name__ == '__main__':
    #gitlist = [git for git in Git.get_gitlist() if 'core-customer' in git.repo]
    gitlist = Git.get_gitlist()
    branch = 'feature/MLFFDEV-22094_MLFF_repository-k_átállítása_a_db-dwh_liquibase_image_használatára'
    #create_branch_multiple_repos(gitlist, branch)
    #create_stage_and_commit(gitlist, 'MLFFDEV-22094  MLFF_repository-k_átállítása_a_db-dwh_liquibase_image_használatára')
    #push_branch(gitlist, branch)
    delete_branch_multiple_repos(gitlist, branch)
