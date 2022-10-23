from Repository import Repository
from liquibase_runner.Runner import Runner
from liquibase_runner.params import repositories, params

if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    repos = repositories
    runner = Runner(base, repos)
    # TODO beletenni maga előtt teljes törlés opciót
    runner.run(params['loc'], params['delete_db_before'], params['checkonly'])
