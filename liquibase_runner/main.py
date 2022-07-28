import os

from Repository import Repository
from Runner import Runner

if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repos = [Repository(name) for name in os.listdir(Repository.base)]
    a = os.listdir('c:/GIT/MLFF/')
    repos = [Repository(x) for x in os.listdir('c:/GIT/MLFF/') if 'mlff-payment' in x]
    #repos = load_from_file('repos.txt')
    repos = [Repository('mlff-enforcement-detection-postgredb')]
    runner = Runner(base, repos)
    #TODO beletenni maga előtt teljes törlés opciót
    runner.run(loc='fit', full=False) #local ,sandbox, remote, dev, fit
