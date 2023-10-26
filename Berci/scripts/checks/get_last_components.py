from tabulate import tabulate

import Repository

l = []
max_rel_filter = '0.21'
for repo in [x for x in Repository.get_all_repos() if 'xxx' not in x.name]:
    #print(repo)
    comp, rel = repo.last_component_ver(max_rel_filter)
    l.append([repo.name , comp, rel])
print(tabulate(l, headers=['Name', 'Comp', 'MLFF rel'], floatfmt=".2f"))