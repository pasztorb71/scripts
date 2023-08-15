from tabulate import tabulate

import Repository

l = []
for repo in [x for x in Repository.get_all_repos() if '' in x.name]:
    l.append([repo.name, repo.env_ver])
print(tabulate(l, floatfmt=".2f"))
#for repo in utils_repo.get_all_repos_by_group('N2O'):
#    print(repo.name, repo.env_ver)
