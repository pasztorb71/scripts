from Repository import Repository
from liquibase_runner.Runner import Runner

repos = [Repository('observation')]
Runner(repos).run_multiple_repos(loc = 'local', checkonly = False)
print('Ne felejtsd el beírni ide: https://confluence.icellmobilsoft.hu/pages/viewpage.action?pageId=144325904')
