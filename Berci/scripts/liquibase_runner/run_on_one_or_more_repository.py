from Repository import Repository
from liquibase_runner.Runner import Runner

repos = [Repository('psp-clea')]
Runner(repos).run_multiple_repos(loc = 'sandbox', checkonly = False)
print('Ne felejtsd el beírni ide: https://confluence.icellmobilsoft.hu/pages/viewpage.action?pageId=144325904')
