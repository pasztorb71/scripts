from Repository import Repository
from liquibase_runner.Runner import Runner

if __name__ == '__main__':
    #repos = [Repository(name) for name in load_from_file('repos.txt')][0:]
    #repos = [Repository(name) for name in Repository().get_repo_names() if 'eee' not in name]
    repos = [Repository('analy')]
    runner = Runner(repos[0:], confirm=False)
    runner.run_multiple_repos('local',
                              delete_db_before=True,
                              checkonly=False,
                              delete_changelog_only=False,
                              deleteonly=True)
