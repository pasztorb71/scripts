from Repository import Repository
from liquibase_runner.Runner import Runner
from liquibase_runner.params import repositories, params
from utils_file import load_from_file

if __name__ == '__main__':
    repo = Repository()
    base = repo.get_base()
    #repos = [Repository(name) for name in load_from_file('repos.txt')]
    #repos = [Repository(name) for name in repo.get_repo_names()]
    repos = [Repository('dispatch')]
    runner = Runner(base, repos)
    runner.run('local',
               delete_db_before=True,
               checkonly=False,
               delete_changelog_only=True)
