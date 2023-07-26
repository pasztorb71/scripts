from Ticket import Ticket


def read_ticket() -> Ticket:
    nr = input('Kérem a ticket számát:')
    t = Ticket(f'MLFFDEV-{nr}')
    return t


def create_branch(t: Ticket) -> None:
    print(f'branch : {t.branch}')
    print(f'release: {t.release}')

if __name__ == '__main__':
    t = read_ticket()
    create_branch(t)
