import utils
from Cluster import Cluster
from Database import Database
from Repository import Repository
from liquibase_runner.Runner import Runner

if __name__ == '__main__':
    base_inst = {'loc' : 'new_dev',
                 'port': get_port(Repository('core').)
                 }
    """
    host, port = 'localhost', 5640
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    databases = cluster.databases[0:]
    """
    #repo_names = repo.get_repo_names()
    #repos = [Repository(x) for x in repo_names]
    #repos = Database.get_repositories_from_dbs(databases)
    repos = [Repository('template-post')]
    Runner(repos).run_multiple_repos(loc = 'local', checkonly = False)
