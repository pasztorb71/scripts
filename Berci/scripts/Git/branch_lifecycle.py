
from Git.Git_class import Git
from Git.services import delete_branch_multiple_repos

if __name__ == '__main__':
    #repolist = [Repository.Repository(r).name for r in ['trip','observ','detection_postg','exemption','visual','analytic']]
    #gitlist = Git.get_gitlist(include=repolist)[0:]
    #repos = Repository.get_repos_filtered_by_funct(filterfunc)
    # Egy konkrét repo
    #r = Repository('customer')
    #gitlist = [Git(r.base, r.name)]
    # Egy konkrét repo end
    gitlist = [git for git in Git.get_gitlist() if 'geo-alert' not in git.repo][0:]
    branch = 'feature/MLFFSUP-152_Release_munkák,_snapsot,_új_release'
    #create_branch_multiple_repos(gitlist, branch)
    #TODO ellenőrizni ha létezik már a branch
    #create_stage_and_commit(gitlist, 'MLFFSUP-152  change_common_version')
    #push_branch(gitlist, branch)
    delete_branch_multiple_repos(gitlist, branch)
