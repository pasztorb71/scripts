import utils
from Database import Database
from Repository import Repository

if __name__ == '__main__':
    repo = Repository()
    repo_names = repo.get_repo_names()
    repos = [Repository(x) for x in repo_names if x.startswith('mlff-core-')]
    for repo in repos:
        db = Database(repo.get_db_name(), 'localhost', utils.get_port('new_sandbox', repo.name))
        print(f'{db.name} adatbázis az {db.port} porton')

            db.truncate_all_tables()