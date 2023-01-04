import utils
from Cluster import Cluster
from Repository import Repository
from utils_db import get_sema_from_dbname
from utils_sec import password_from_file


def print_create_databases(port, databases):
    print(f'---  {port} ---')
    for db in databases:
        print(f"""CREATE DATABASE {db} WITH 
  OWNER = postgres
  ENCODING = 'UTF8'
  CONNECTION LIMIT = -1;
""")

def print_dump_databases(port, databases):
    print()
    for db in databases:
        print(f'pg_dump -p 5435 -U postgres -Fc --verbose {db} >{db}.dump')
        print(f'pg_restore -p {port} -U postgres --verbose -d {db} {db}.dump')

def print_grants_databases(port, databases):
    print(f'---  {port} ---')
    for db in databases:
        sema = get_sema_from_dbname(db)
        print(f'GRANT USAGE ON SCHEMA {sema} TO {sema}_sel;')
        print(f'GRANT USAGE ON SCHEMA {sema} TO {sema}_tbl_own;')

def copy_fit():
    host, port = 'localhost', utils.get_port('fit')
    for port in list(range(5640, 5647)):
        cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
        databases = cluster.databases[0:]
        #print_create_databases(port, databases)
        #print_dump_databases(port, databases)
        print_grants_databases(port, databases)


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