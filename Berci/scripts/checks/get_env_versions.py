from tabulate import tabulate

import utils_repo

for repo in utils_repo.get_all_repos():
    print(repo.name, repo.env_ver)
