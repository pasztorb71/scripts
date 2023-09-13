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
    return pass_out