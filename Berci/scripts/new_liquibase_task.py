from Git.Git_class import Git
from Repository import Repository
from Ticket import Ticket


def read_ticket() -> Ticket:
    nr = input('Number of ticket?:')
    t = Ticket(f'MLFFSUP-{nr}')
    return t


def create_branch(t: Ticket, r: Repository) -> None:
    git = Git(repo=r)
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


if __name__ == '__main__':
    repo = Repository('-detection-pos')
    print(repo.name)
    t = read_ticket()
    print_info(t, repo)
    create_branch(t, repo)
    table_operations()

