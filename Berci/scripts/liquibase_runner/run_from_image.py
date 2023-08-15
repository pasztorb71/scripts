import os

from Repository import Repository


def run_images(repos):
    for cmd in [repo.image_run_command for repo in repos]:
        print(cmd)
        """
        if input("Mehet a telepítés? [y/n]") != "y":
            print('Telepítés megszakítva!')
            exit(0)
        """
        ret_code = os.system(cmd)
        if ret_code != 0:
            exit(ret_code)


if __name__ == '__main__':
    repos = [Repository(x) for x in Repository.get_repo_names() if 'onsite-inspection' in x]
    #print('\n'.join(repo.image_build_command for repo in repos))
    run_images(repos)
