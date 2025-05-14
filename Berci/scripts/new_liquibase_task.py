from Git.Git_class import Git
from classes.Project import choose_project, base_from_project
from classes.Repository import Repository
from classes.Ticket import Ticket


def read_ticket(project) -> Ticket:
    nr = input('Number of ticket?:')
    t = Ticket(f'{project}-{nr}')
    return t


def create_branch(t: Ticket, r: Repository, base=None) -> None:
    git = Git(repo=r.name, base=base)
    print(f'Current branch: {git.current_branch}')
    if git.current_branch != 'master':
        print('EXIT')
        exit(1)
    if input("Create branch? [y/n]") == "y":
        git.new_branch(t.branch)
        return True



def print_info(t: Ticket, r: Repository):
    print(f'branch : {t.branch}')
    print(f'commit msg : {t.commit_msg}')
    print(f'release: {t.release}')
    print(f'release in repo: {r.env_ver}')


def table_operations():
    #TODO table operations
    pass


def check_xml_path():
    #TODO implementálni
    pass


if __name__ == '__main__':
    #reponame = 'backend' #AKP
    reponame = 'trino'
    #reponame = 'meta'
    #reponame = 'parser'
    proj = choose_project(reponame)
    base = base_from_project(proj)
    repo = Repository(reponame, proj=proj)
    print(repo.name)
    t = read_ticket(proj)
    print_info(t, repo)
    create_branch(t, repo, base=base)
    print("""Confluence-n módosítani
    Antora-ban módosítani""")
    check_xml_path()
    table_operations()

