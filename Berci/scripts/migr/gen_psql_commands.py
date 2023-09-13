import Environment
from Cluster import Cluster
from Gcloud import get_instance_email
from utils.utils_db import get_sema_from_dbname


def gen_bucket_write_rights(project, instances) -> list:
    out = []
    for instance in instances:
        print(instance)
        email = get_instance_email('mlff-sb', instance)
        out.append(f'gsutil iam ch serviceAccount:{email}:roles/storage.objectCreator gs://backup-teszt')
    return out


def gen_bucket_read_rights(project, instances) -> list:
    out = []
    for instance in instances:
        print(instance)
        email = get_instance_email(project, instance)
        out.append(f'gsutil iam ch serviceAccount:{email}:roles/storage.objectViewer gs://backup-teszt')
    return out


def write_main_bat(ports):
    commands = [f'@SET PGPASSWORD={new_password}']
    for port in ports:
        commands.append(f'psql -p {port} -U postgres -d postgres -q -f psql_commands_{port}.sql')
    with open('c:/Users/bertalan.pasztor/Documents/MLFF/migr/new_psql.bat', 'w') as f:
        f.write('\n'.join(commands))


def write_psql_files(from_ports, to_ports):
    for idx, port in enumerate(from_ports[0:]):
        commands = []
        cluster = Cluster(port, password)
        dbnames = cluster.databases
        for db in dbnames:
            print(db)
            commands.append(f'DROP DATABASE IF EXISTS {db};')
            commands.append(f"""CREATE DATABASE {db} WITH
  OWNER = postgres
  ENCODING = 'UTF8'
  CONNECTION LIMIT = -1;\n""")
        with open(f'c:/Users/bertalan.pasztor/Documents/MLFF/migr/psql_commands_{to_ports[idx]}.sql', 'w') as f:
            f.write('\n'.join(commands))


def write_main_privileges_bat(ports):
    commands = [f'@SET PGPASSWORD={new_password}']
    for port in ports:
        commands.append(f'psql -p {port} -U postgres -d postgres -q -f psql_privilege_commands_{port}.sql')
    with open('c:/Users/bertalan.pasztor/Documents/MLFF/migr/new_privileges_psql.bat', 'w') as f:
        f.write('\n'.join(commands))


def write_psql_privilege_files(from_ports, to_ports):
    for idx, port in enumerate(from_ports[0:]):
        commands = []
        cluster = Cluster(port, password)
        dbnames = cluster.databases
        for db in dbnames:
            print(db)
            commands.append(f'\c {db};')
            sema = get_sema_from_dbname(db)
            commands.append(f"SET search_path = {sema};")
            commands.append(f"call add_privileges_to_all_tables('{sema}');\n")
        with open(f'c:/Users/bertalan.pasztor/Documents/MLFF/migr/psql_privilege_commands_{to_ports[idx]}.sql', 'w') as f:
            f.write('\n'.join(commands))



if __name__ == '__main__':
    project = 'mlff-dev'
    password = 'fLXyFS0RpmIX9uxGII4N'
    new_password = 'zsxQ4RUkdOTev8k7bxgU'
    from_ports = Environment.get_ports('dev')
    to_ports = Environment.get_ports('new')
    write_main_bat(to_ports)
    write_psql_files(from_ports, to_ports)
    write_main_privileges_bat(to_ports)
    write_psql_privilege_files(from_ports, to_ports)

