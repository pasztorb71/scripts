from tabulate import tabulate

import utils_repo

l = []
for repo in [x for x in utils_repo.get_all_repos() if 'xxx' not in x.name]:
    l.append([repo.name, repo.env_ver])
print(tabulate(l, floatfmt=".2f"))
#for repo in utils_repo.get_all_repos_by_group('N2O'):
#    print(repo.name, repo.env_ver)
