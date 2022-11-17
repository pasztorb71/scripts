from Repository import Repository
from liquibase_runner.Runner import Runner
from liquibase_runner.params import repositories, params

if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repo_names = repo.get_repo_names()
    #repos = [Repository(x) for x in repo_names if not x.startswith('mlff-core-')]
    repos = repositories
    runner = Runner(base, repos)
    # TODO beletenni maga előtt teljes törlés opciót
    runner.run(params['loc'], params['delete_db_before'], params['checkonly'])
