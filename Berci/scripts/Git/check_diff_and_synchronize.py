import Repository

from Git.Git_class import Git
from Git.services import is_branch_synchronized_in_multiple_repos, synchronize_branch_in_multiple_repos, \
    create_branch_multiple_repos
import utils


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


if __name__ == '__main__':
    gitlist = [git for git in Git.get_gitlist() if '' in git.repo]
    #gitlist = Git.get_gitlist()
    check_diff_and_synchronize()
    #synchronize_branch_in_multiple_repos(gitlist, branch='master')
