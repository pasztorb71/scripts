from Repository import Repository
from liquibase_runner.Runner import Runner
from liquibase_runner.params import repositories, params
from utils import load_from_file

if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repos = [Repository(name) for name in load_from_file('repos.txt')]
    repos = [Repository(name) for name in repo.get_repo_names()]
    #repos = [Repository('genos-')]
    runner = Runner(base, repos)
    # TODO beletenni maga előtt teljes törlés opciót
    runner.run('local', True, False)
