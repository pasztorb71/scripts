import logging
from Repository import Repository
from liquibase_runner.Runner import Runner
from liquibase_runner.params import repositories, params
from utils_file import load_from_file

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, filename='liquibase_run.log', filemode='a', format='%(asctime)s - %(message)s')
    repo = Repository()
    base = repo.get_base()
    #repo_names = repo.get_repo_names()
    #repos = [Repository(x) for x in repo_names]
    repos = repositories
    runner = Runner(base, repos)
    # TODO beletenni maga előtt teljes törlés opciót
    runner.run(params['loc'], params['delete_db_before'], params['checkonly'], log=True)
