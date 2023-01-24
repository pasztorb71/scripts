from Repository import Repository
from liquibase_runner.Runner import Runner

repos = [Repository('tariff')]
Runner(repos).run_multiple_repos(loc = 'sandbox', checkonly = False)
