from Repository import Repository
from liquibase_runner.Runner import Runner

repos = [Repository('-wa')]
#repos = [Repository(x) for x in Repository.get_repo_names() if '-detection' in x]
Runner(repos).run_multiple_repos(loc = 'local', checkonly = False)
print('Ne felejtsd el beírni ide: https://confluence.icellmobilsoft.hu/pages/viewpage.action?pageId=144325904')
