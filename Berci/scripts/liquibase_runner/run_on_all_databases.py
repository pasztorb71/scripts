from Database import Database
from Environment import Env
from liquibase_runner.Runner import Runner

if __name__ == '__main__':
    e = Env('dev')
    x = e.database_names[23:]
    repos = Database.get_repositories_from_dbs(x)
    Runner(repos, confirm=False).run_multiple_repos(loc = 'new', checkonly = False)
