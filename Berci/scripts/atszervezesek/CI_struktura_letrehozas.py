import os

from Git.Git_class import git_init
from utils_db import get_db_name
from utils_file import copy_dir, replace_in_file, copy_file


def _cre_docker_compose_build(fname):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(""".docker-compose-build:
  build-push:
    - docker-compose --env-file .env -f etc/release/docker-compose.yml build
    - !reference [.docker-script, test]
    - etc/release/release.sh
    - !reference [.docker-script, test]
""")

def create_file(fname):
    if 'docker-compose-build.yml' in fname:
        _cre_docker_compose_build(fname)

if __name__ == '__main__':
  # prepare
    repo = 'mlff-liquibase-common-postgredb'
    base = 'c:/GIT/'+repo
    #base = 'c:/GIT/MLFF/'+repo
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    to_replace = [['core-customer', db],['core_customer', db_path]]
  #work
    #git_init(base)
    #exit(0)
    copy_dir('c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\.gitlab\\', base+'/.gitlab', delete_dir_if_exists=True)
    copy_dir('c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\docs\\', base+'/docs', delete_dir_if_exists=True)
    replace_in_file(base+'/docs/development.adoc', to_replace)
    replace_in_file(base+'/docs/release-flow.adoc', to_replace)
    copy_dir('c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\etc\\', base+'/etc', delete_dir_if_exists=True)
    replace_in_file(base+'/etc/docker-compose/docker-compose.postgredb.yml', to_replace)
    replace_in_file(base+'/etc/docker-compose/docker-compose.liquibase.install.step-01.yml', to_replace)
    replace_in_file(base+'/etc/docker-compose/docker-compose.liquibase.install.step-02.yml', to_replace)
    path = base+'/etc/docker-compose/config/'
    os.rename(path+'core_customer', path+db_path)
    replace_in_file(base+'/etc/docker-compose/config/'+db_path+'/step-01/liquibase-localhost.properties', to_replace)
    replace_in_file(base+'/etc/docker-compose/config/'+db_path+'/step-02/liquibase-localhost.properties', to_replace)
    path = base+'/etc/release/'
    replace_in_file(path+'docker-compose.yml', to_replace)
    replace_in_file(path+'release.sh', to_replace)
    os.system('git -C '+base+' add '+path+'release.sh')
    os.system('git -C '+base+' update-index --chmod=+x '+path+'release.sh')
    path = 'c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\'
    copy_file(path+'run.sh', base+'/run.sh')
    os.system('git -C ' + base + ' add ' + 'run.sh')
    os.system('git -C ' + base + ' update-index --chmod=+x ' + 'run.sh')
    copy_file(path+'.gitignore', base+'/.gitignore')
    copy_file(path+'.gitlab-ci.yml', base+'/.gitlab-ci.yml')
    copy_file(path+'.env', base+'/.env')
    replace_in_file(base+'/.env', to_replace)
  #readme file
    copy_file(r'c:\GIT\MLFF\mlff-core-customer-postgredb\OLD-README.md', base+'/OLD-README.md')
    replace_in_file(base+'/OLD-README.md', to_replace)
    copy_file(r'c:\GIT\MLFF\mlff-core-customer-postgredb\README.adoc', base+'/README.adoc')
    replace_in_file(base+'/README.adoc', to_replace)
  #post
    #replace_in_file(base+'/.env', [['VERSION=0.4.0', 'VERSION=0.2.0']])
