import Repository

from Git.Git_class import Git
from Git.services import create_stage_and_commit, push_branch, delete_branch_multiple_repos, \
    create_branch_multiple_repos

if __name__ == '__main__':
    #gitlist = Git.get_gitlist(exclude=[''])
    gitlist = Git.get_gitlist(exclude=['empty'])[0:]
    names = "core-analytic,core-vehicle,customer,eobu-tariff,eobu-trip,exemption,obu-obuprovider,privateuser,ticket,vehicle"
    n1 = names.split(',')
    gitlist = [x for x in gitlist if any([(i in x.repo) for i in n1])]
    print('\n'.join([g.repo for g in gitlist]))
    exit(0)
    branch = 'feature/MLFFSUP-1521_Release_munkák,_snapsot,_új_release'
    #create_branch_multiple_repos(gitlist, branch)
    #create_stage_and_commit(gitlist, 'MLFFSUP-1521  Version to 1.1')
    #push_branch(gitlist, branch)
    delete_branch_multiple_repos(gitlist, branch)
