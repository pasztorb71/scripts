import os

from Repository import Repository
from liquibase_runner.Runner import Runner
from liquibase_runner.params import repositories, params


def confirm_old(repos, loc):
    print(f"Az alábbi repokra lesz telepítve, host: {loc}")
    for r in repos:
        print(f" - {r.get_name()}")
    if input("Mehet a telepítés? [y/n]") == "y":
        return True
    return False


if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repos = repositories
    runner = Runner(base, repos)
    # TODO beletenni maga előtt teljes törlés opciót
    runner.run(params['loc'], params['full'], params['checkonly'])
