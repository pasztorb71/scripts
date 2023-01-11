from Repository import Repository
from liquibase_runner.Runner import Runner

repos = [Repository('trip')]
Runner(repos).run_multiple_repos(loc = 'new_sandbox', checkonly = False)
