"""
A program felolvassa a fájlt, majd a fájlban található repository nevek melletti verziószámok szerint
chckoutolja a megfelelő releae verziókat a megadott repository-kban
"""
from Git.Git_class import Git

FILENAME = 'checkout_file.txt'

def get_reponame_from_dbname(dbname):
    return f"mlff-{dbname.replace('_', '-')}-postgredb"

def get_repolist_from_file(filename=FILENAME):
    global f, lines
    with open(filename, 'r') as f:
        lines = f.readlines()
    repolist = [get_reponame_from_dbname(r.split(':')[0]) for r in lines]
    return repolist

if __name__ == '__main__':
    repolist = get_repolist_from_file()
    gitlist = Git.get_gitlist(include=repolist)
    git_dict = {git.repo: git.get_remote_releases() for git in gitlist}
    version_dict = {}
    with open(FILENAME, 'r') as f:
        for line in f.readlines():
            repo = get_reponame_from_dbname(line.split(':')[0])
            version_dict[repo] = line.split(':')[1].strip()
    for line in lines:
        dbname, version = line.split(':')
        repo = get_reponame_from_dbname(dbname)
        print(f'Checking out {version.strip()} in {repo}')
        print('\n'.join(git_dict[repo]))
        #os.system(f'cd /c/Users/bertalan.pasztor/Documents/REPOS/{repo} && git checkout {version}')
        print(f'Checked out {version.strip()} in {repo}')
