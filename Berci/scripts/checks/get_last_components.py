import utils_repo

for repo in utils_repo.get_all_repos():
    print(repo.name, repo.last_component_ver)
