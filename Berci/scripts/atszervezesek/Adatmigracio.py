from Database import Database
from Repository import Repository

if __name__ == '__main__':
    repo = Repository()
    repo_names = repo.get_repo_names()
    repos = [Repository(x) for x in repo_names if x.startswith('mlff-core-')]
    for repo in repos:
        db = Database()
