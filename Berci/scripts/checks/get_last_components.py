from tabulate import tabulate

import utils_repo

l = []
for repo in [x for x in utils_repo.get_all_repos() if 'xxx' not in x.name]:
    l.append([repo.name, repo.last_component_ver])
print(tabulate(l, floatfmt=".2f"))