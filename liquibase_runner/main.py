import os

from Repository import Repository
from Runner import Runner

if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repos = [Repository(name) for name in os.listdir(Repository.base)]
    #repos = [x for x in repos if 'enforcement' in x]
    #repos = load_from_file('repos.txt')
    repos = [repo.get_name('psp-clearing')]
    runner = Runner(base)
    #TODO beletenni maga előtt teljes törlés opciót
    runner.run(repos, loc='local', full=False) #local ,sandbox, remote, dev, fit
