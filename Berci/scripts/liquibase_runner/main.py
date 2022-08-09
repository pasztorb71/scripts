import os

from Repository import Repository
from liquibase_runner.Runner import Runner

if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repos = [Repository(name) for name in os.listdir(Repository.base)]
    repos = [Repository(x) for x in os.listdir('c:/GIT/MLFF/') if 'eligibility' in x]
    #repos = load_from_file('repos.txt')
    repos = [Repository('customer')]
    runner = Runner(base, repos)
    #TODO beletenni maga előtt teljes törlés opciót
    runner.run(loc='dev', full=False, checkonly=False) #local ,sandbox, remote, dev, fit
