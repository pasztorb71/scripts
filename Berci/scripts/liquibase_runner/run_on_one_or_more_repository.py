from Repository import Repository
from liquibase_runner.Runner import Runner

repos = [Repository('customer-')]
Runner(repos).run_multiple_repos(loc = 'local', checkonly = False)
