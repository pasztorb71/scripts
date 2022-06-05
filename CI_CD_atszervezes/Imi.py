import os
import re

from CI_CD_atszervezes.utils import copy_dir, replace_in_file, copy_file, move_file


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

def get_schema():
    with open(base+'/liquibase/'+db_path+'/_init_dbs/' + db_path + '-db-install-parameters.xml', 'r', encoding='utf-8') as f:
        text = f.read()
    return re.match('.*property name="schema_name_.*value="(.*)"/>', text, flags=re.DOTALL|re.MULTILINE).group(1)

if __name__ == '__main__':
    repo = 'mlff-core-vehicle-postgredb'
    base = 'c:/GIT/MLFF/'+repo
    db = re.match('.*mlff-(.*)-postgredb', base).group(1)
    db_path = db.replace('-', '_')
    to_replace = [['core-customer', db],['core_customer', db_path]]
    copy_dir('c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\.gitlab\\', base+'/.gitlab')
    copy_dir('c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\docs\\', base+'/docs')
    replace_in_file(base+'/docs/development.adoc', to_replace)
    replace_in_file(base+'/docs/release-flow.adoc', to_replace)
    copy_dir('c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\etc\\', base+'/etc')
    replace_in_file(base+'/etc/docker-compose/docker-compose.postgredb.yml', to_replace)
    replace_in_file(base+'/etc/docker-compose/docker-compose.liquibase.install.step-01.yml', to_replace)
    replace_in_file(base+'/etc/docker-compose/docker-compose.liquibase.install.step-02.yml', to_replace)
    path = base+'/etc/docker-compose/config/'
    os.rename(path+'core_customer', path+db_path)
    replace_in_file(base+'/etc/docker-compose/config/core_vehicle/step-01/liquibase-localhost.properties', to_replace)
    replace_in_file(base+'/etc/docker-compose/config/core_vehicle/step-02/liquibase-localhost.properties', to_replace)
    path = base+'/etc/release/'
    replace_in_file(path+'docker-compose.yml', to_replace)
    replace_in_file(path+'release.sh', to_replace)
    os.system('git -C '+base+' add '+path+'release.sh')
    os.system('git -C '+base+' update-index --chmod=+x '+path+'release.sh')
    path = 'c:\\GIT\\MLFF\\mlff-core-customer-postgredb\\'
    copy_file(path+'.gitignore', base+'/.gitignore')
    copy_file(path+'.gitlab-ci.yml', base+'/.gitlab-ci.yml')
    copy_file(path+'.env', base+'/.env')
    replace_in_file(base+'/.env', to_replace)
    copy_file(path+'.asciidoctorconfig.adoc', base+'/.asciidoctorconfig.adoc')
  #readme file
    move_file(base+'/README.md', base+'/liquibase/'+db_path+'/OLD-README.md')
    copy_file(r'c:\GIT\MLFF\mlff-core-customer-postgredb\README.adoc', base+'/README.adoc')
    replace_in_file(base+'/README.adoc', to_replace)
