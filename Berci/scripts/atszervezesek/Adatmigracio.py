import Environment
from Cluster import Cluster
from utils.utils_db import get_sema_from_dbname
from utils.utils_sec import password_from_file


def print_create_databases(port, databases):
    print(f'---  {port} ---')
    for db in databases:
        print(f"""CREATE DATABASE {db} WITH 
  OWNER = postgres
  ENCODING = 'UTF8'
  CONNECTION LIMIT = -1;
""")

def print_dump_databases(port, databases):
    print()
    for db in databases:
        print(f'pg_dump -p 5435 -U postgres -Fc --verbose {db} >{db}.dump')
        print(f'pg_restore -p {port} -U postgres --verbose -d {db} {db}.dump')

def print_grants_databases(port, databases):
    print(f'---  {port} ---')
    for db in databases:
        sema = get_sema_from_dbname(db)
        print(f'GRANT USAGE ON SCHEMA {sema} TO {sema}_sel;')
        print(f'GRANT USAGE ON SCHEMA {sema} TO {sema}_tbl_own;')


def get_instance_name_from(port, base_port):
    for i in Environment.Env.offset.items():
        if port-base_port == i[1]:
            return i[0]


def is_database_in_instance(db, instance_name):
    if db == 'document' and instance_name == 'pg-doc':
        return True
    if db.split('_')[0] == instance_name.split('-')[1]:
        return True
    return False


def copy_db(from_env, to_range):
    host, port = 'localhost', Environment.get_port_from_env_repo(from_env)
    cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
    databases = cluster.databases[0:]
    base_port = min(list(to_range))
    for port in list(to_range):
        instance_name = get_instance_name_from(port, base_port)
        dblist = [db for db in databases if is_database_in_instance(db, instance_name)]
        print_create_databases(port, dblist)
    for port in list(to_range):
        instance_name = get_instance_name_from(port, base_port)
        dblist = [db for db in databases if is_database_in_instance(db, instance_name)]
        print_dump_databases(port, dblist)
    for port in list(to_range):
        instance_name = get_instance_name_from(port, base_port)
        dblist = [db for db in databases if is_database_in_instance(db, instance_name)]
        print_grants_databases(port, dblist)


if __name__ == '__main__':
    copy_db(from_env='test',
            to_range=range(5840, 5847))
