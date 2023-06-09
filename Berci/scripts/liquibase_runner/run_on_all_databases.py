import utils
from Cluster import Cluster
from Database import Database
from Environment import Env
from Repository import Repository
from liquibase_runner.Runner import Runner
from utils_file import load_from_file
from utils_repo import get_repos_from_port

if __name__ == '__main__':
    e = Env('test')
    x = e.database_names[18:-1]
    repos = Database.get_repositories_from_dbs(x)
    Runner(repos, confirm=False).run_multiple_repos(loc = 'test', checkonly = False)
