from Repository import Repository
from liquibase_runner.Runner import Runner

if __name__ == '__main__':
    #repos = [Repository(name) for name in load_from_file('repos.txt')][0:]
    #repos = [Repository(name) for name in Repository().get_repo_names() if 'enforcement_eligibility' not in name]
    repos = [Repository('private')]
    runner = Runner(repos, confirm=False)
    runner.run_multiple_repos('local',
                              delete_db_before=True,
                              checkonly=False,
                              delete_changelog_only=False)
