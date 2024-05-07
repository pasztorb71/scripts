
from Git.Git_class import Git
from Git.services import create_stage_and_commit, push_branch, delete_branch_multiple_repos, \
    create_branch_multiple_repos
import Repository

if __name__ == '__main__':
    repolist = [Repository.Repository(r).name for r in ['trip','observ','detection_postg','exemption','visual','analytic']]
    gitlist = Git.get_gitlist(include=repolist)[0:]
    #repos = Repository.get_repos_filtered_by_funct(filterfunc)
    # Egy konkrét repo
    #r = Repository('customer')
    #gitlist = [Git(r.base, r.name)]
    # Egy konkrét repo end
    branch = 'feature/MLFFSUP-8148_Transform_PlateNumber_lower_to_upper_in_whole_system'
    create_branch_multiple_repos(gitlist, branch)
    #TODO ellenőrizni ha létezik már a branch
    #create_stage_and_commit(gitlist, 'MLFFDEV-18914  fix db names')
    #push_branch(gitlist, branch)
    #delete_branch_multiple_repos(gitlist, branch)
