import sql_runner
from sql_runner.parallel_runner.multiprocess import gen_port_databases_from_envs, parallel_run_multiprocess, \
    mproc_get_tables
from utils import utils
from utils.utils_db import get_sema_from_dbname
from utils.utils_file import get_files_from_path_ext_filtered


def get_dump_commands(ports_databases, path, return_dict):
    out = []
    for port_db in ports_databases:
        c = get_dump_command(port_db[0], port_db[1], path, return_dict[port_db[1]+'|'+port_db[0]])
        out.append([port_db[1], c])
    return out

def get_dump_command(port, db, path, dictdata ):
    sema = get_sema_from_dbname(db)
    c = f'pg_dump -h localhost -p {port} -d {db} -U postgres -s -F p -E UTF-8 -n {sema} ^\n'
    for row in dictdata[1:]:
        c += f'-t {row[0]}.{row[1]}  ^\n'
    c += f'-f {path}{db}.sql'
    return c


def make_dumps(env, path, return_dict=None):
    ports_databases = gen_port_databases_from_envs([env])[0:]
    dump_commands = get_dump_commands(ports_databases, path, return_dict)
    with open(path + 'run_all.bat', 'w') as f_all:
        for data in dump_commands:
            with open(path + f'run_{data[0]}.bat', 'w') as f_db:
                f_db.write('@SET PGPASSWORD=zsxQ4RUkdOTev8k7bxgU\n')
                f_db.write(data[1] + '\n')
            f_all.write(f'start run_{data[0]}.bat\n')


def filter_sql(data):
    out = []
    started = False
    for l in data:
        if started == True and l.startswith('GRANT USAGE '):
            break
        if started == False and l.startswith('CREATE TABLE '):
            started = True
        if started == True:
            if not l.startswith('--') and l != '\n':
                out.append(l)
    return out

def make_filetered_dumps(path):
    files = get_files_from_path_ext_filtered(path, 'sql')
    for file in files:
        orig_fname = file.rsplit('\\',1)[1]
        if orig_fname.startswith('f_'):
            continue
        fname = 'f_' + file.rsplit('\\',1)[1]
        with open(file, 'r') as f:
            data = f.readlines()
            filtered_sql = filter_sql(data)
            with open(path + fname, 'w') as outf:
                outf.writelines(filtered_sql)

if __name__ == '__main__':
    path = 'c:\\Users\\bertalan.pasztor\\Documents\\MLFF\\Diagrams\\'
    env = 'tollgo'
    ports_databases = gen_port_databases_from_envs([env], forced_refresh=False)[0:]
    return_dict = sql_runner.parallel_runner.multiprocess.parallel_run_multiprocess(ports_databases, mproc_get_tables)
    make_dumps(env, path, return_dict)
