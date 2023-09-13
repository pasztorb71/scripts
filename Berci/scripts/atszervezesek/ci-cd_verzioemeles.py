import Environment
from Database import Database
from Repository import Repository

if __name__ == '__main__':
    repo = Repository()
    repo_names = repo.get_repo_names()
    repos = [Repository(x) for x in repo_names if x.startswith('')]
    for repo in repos[0:1]:
        db_to = Database(repo.get_db_name(), 'localhost', Environment.get_port_from_env_repo('new_sandbox', repo.name))
        db_to = Database(repo.get_db_name(), 'localhost', Environment.get_port_from_env_repo('new_sandbox', repo.name))
        print(f'{db.name} adatbázis az {db.port} porton')
        db.dump_database()
        triggers = db.triggers
        db.remove_all_hist_triggers()
        if input("Kész a migráció?[y/n]") == "y":
            pass
        db.put_triggers(triggers)