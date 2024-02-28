
from Git.Git_class import Git
from Git.services import create_stage_and_commit, push_branch, delete_branch_multiple_repos, \
    create_branch_multiple_repos
from Repository import Repository

if __name__ == '__main__':
    #gitlist = Git.get_gitlist(exclude=['info','inspection'])[0:]
    # Egy konkrét repo
    r = Repository('customer')
    gitlist = [Git(r.base, r.name)]
    # Egy konkrét repo end
    branch = 'feature/MLFFDEV-18914-liquibase-refakt_common_inside'
    create_branch_multiple_repos(gitlist, branch)
    #TODO ellenőrizni ha létezik már a branch
    #create_stage_and_commit(gitlist, 'MLFFDEV-18914  fix db names')
    #push_branch(gitlist, branch)
    #delete_branch_multiple_repos(gitlist, branch)
