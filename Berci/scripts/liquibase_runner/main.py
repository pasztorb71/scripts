import os

from Repository import Repository
from liquibase_runner.Runner import Runner


def confirm(repos):
    print("Az alábbi repokra lesz telepítve:")
    for r in repos:
        print(f" - {r.get_name()}")
    if input("Mehet a telepítés? [y/n]") == "y":
        return True
    return False


if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repos = [Repository(name) for name in os.listdir(Repository.base)]
    repos = [Repository(x) for x in os.listdir('c:/GIT/MLFF/') if 'visual' in x]
    #repos = load_from_file('repos.txt')
    #repos = [Repository('enforcement-detection')]
    runner = Runner(base, repos)
    #TODO beletenni maga előtt teljes törlés opciót
    if not confirm(repos):
        exit(0)
    runner.run(loc='perf', full=False, checkonly=True) #local ,sandbox, remote, dev, fit, perf
