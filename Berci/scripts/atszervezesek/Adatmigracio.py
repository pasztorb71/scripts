import utils
from Database import Database
from Repository import Repository


def copy_fit():
    Cluster


if __name__ == '__main__':
    copy_fit()
    exit(0)
    repo = Repository()
    repo_names = repo.get_repo_names()
    repos = [Repository(x) for x in repo_names if x.startswith('')]
    for repo in repos:
        db_to = Database(repo.get_db_name(), 'localhost', utils.get_port('new_sandbox', repo.name))
        db_to = Database(repo.get_db_name(), 'localhost', utils.get_port('new_sandbox', repo.name))
        print(f'{db.name} adatbázis az {db.port} porton')
        db.dump_database()
        triggers = db.triggers
        db.remove_all_hist_triggers()
        if input("Kész a migráció?[y/n]") == "y":
            pass
        db.put_triggers(triggers)