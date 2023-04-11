from tabulate import tabulate

import utils_repo

l = []
for repo in utils_repo.get_all_repos():
    l.append([repo.name, repo.last_component_ver])
print(tabulate(l, floatfmt=".2f"))