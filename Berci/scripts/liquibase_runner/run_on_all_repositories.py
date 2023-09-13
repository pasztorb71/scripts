from Repository import Repository
from liquibase_runner.Runner import Runner

if __name__ == '__main__':
    repos = [Repository(x) for x in Repository.get_repo_names_exclude(['meta','eligibility'])]
    #repos = [Repository(name) for name in load_from_file('repos.txt')]
    #repos = get_repos_from_port(5438)
    #repos = [Repository('template-post')]
    Runner(repos, confirm=False).run_multiple_repos(loc = 'test', checkonly = False)
