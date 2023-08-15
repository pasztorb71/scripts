import os
from datetime import datetime

import Environment
import Repository
import utils
import utils_db
import utils_sec


def compare_db(dbname, env1, env2):
    repo_name = Repository.get_repository_name_from_dbname(dbname)
    port1 = Environment.get_port_from_env_repo(env1, repo_name)
    port2 = Environment.get_port_from_env_repo(env2, repo_name)
    cmd = f'docker run --rm ' \
          f'liquibase/liquibase:latest ' \
          f'--url=jdbc:postgresql://gateway.docker.internal:{port1}/{dbname} ' \
          f'--driver=org.postgresql.Driver ' \
          f'--username=postgres ' \
          f'--password={utils_sec.password_from_file("postgres",port1)} ' \
          f'--schemas={utils_db.get_sema_from_dbname(dbname)} ' \
          f'diff ' \
          f'--referenceUrl=jdbc:postgresql://gateway.docker.internal:{port2}/{dbname} ' \
          f'--referenceUsername=postgres ' \
          f'--referencePassword={utils_sec.password_from_file("postgres",port2)} ' \
          f'--schemas={utils_db.get_sema_from_dbname(dbname)}'
    print('Diff runs...')
    result = os.popen(cmd).read()
    filename = f'diff_{dbname}_{env1}_{env2}_{str(datetime.now().strftime("%Y%m%d_%H%M%S"))}.txt'
    path = f'c:\\Users\\bertalan.pasztor\\Documents\\MLFF\\PYTHON_OUT\\diff\\{filename}'
    with open(path, 'w') as f:
        f.write(result)
    print('Diff finished.')
    print(f'Eredmény a {path} fájlban')


if __name__ == '__main__':
    compare_db('enforcement_sanctioning_presumption', 'sandbox', 'dev')
