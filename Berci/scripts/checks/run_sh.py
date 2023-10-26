import Repository

repos = Repository.get_all_repos()
for repo in repos:
    print(repo.run_sh_eol_type.ljust(10) + ':', end='')
    print(repo.name)
