from inspect import getfile


def password_from_file(puser, pport, phost='localhost'):
    pass_out = ''
    with open(getfile(password_from_file).rsplit('\\',1)[0] + '\\db_passw.txt', 'r') as f:
        for line in f.read().split('\n'):
            if line.startswith('#'):
                continue
            try:
                user, host, port, passw = line.split()
            except Exception as e:
                print(line)
                raise(e)
            if '_service' in puser and '_service' in user:
                pass_out = passw
                break
            if host == phost and port == str(pport) and user == puser:
                pass_out = passw
                break
        if not pass_out:
            print(f'Nincs jelszó: {puser}, {pport}, {phost}')
    return pass_out


def get_atlassian_login_from_file():
    with open(getfile(get_atlassian_login_from_file).rsplit('\\', 1)[0] + '/icell_passw.txt', 'r') as f:
        return f.readlines()[0].split()

def get_nexus_login_from_file():
    with open(getfile(get_atlassian_login_from_file).rsplit('\\', 1)[0] + '/icell_passw.txt', 'r') as f:
        return f.readlines()[1].split()