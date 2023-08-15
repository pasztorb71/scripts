from tabulate import tabulate

import Repository

l = []
for repo in [x for x in Repository.get_all_repos() if 'xxx' not in x.name]:
    l.append([repo.name, repo.last_component_ver])
print(tabulate(l, floatfmt=".2f"))