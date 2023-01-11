import logging
from datetime import datetime

import utils
from Cluster import Cluster
from Repository import Repository
from liquibase_runner.Runner import Runner
from utils_sec import password_from_file

if __name__ == '__main__':
    host, port = 'localhost', utils.get_port('test')
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    databases = cluster.databases[0:]
    repo = Repository()
    base = repo.get_base()
    repo_names = repo.get_repo_names()
    repos = [Repository(x) for x in repo_names]
    #repos = repositories
    runner = Runner(base, repos)
    runner.run_multiple_repos(params['loc'], params['delete_db_before'], params['checkonly'], log=True)
