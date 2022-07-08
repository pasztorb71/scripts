import os
import shutil

from utils import *


def docker_image_hely_modositas(repos):
  # MLFFDEV-2513  Docker image hely módosítása
  to_replace = [['dockerhub.icellmobilsoft.hu', 'dockerhub-mlff-group.icellmobilsoft.hu']]
  for repo in repos[1:]:
    replace_in_file(base+repo+'/docs/development.adoc', to_replace)
    replace_in_file(base+repo+'/etc/docker-compose/docker-compose.liquibase.install.step-01.yml', to_replace)
    replace_in_file(base+repo+'/etc/docker-compose/docker-compose.liquibase.install.step-02.yml', to_replace)
    replace_in_file(base+repo+'/etc/release/docker-compose.yml', to_replace)

def change_file(fname):
  create_old_file(fname)
  out = open(fname, 'w', encoding='utf-8')
  if 'liquibase-install-step-01.xml' in fname:
    with open(fname+'_old', 'r', encoding='utf-8') as f:
      text = f.read()
      text = text.replace("""    <!-- =================================================================================== -->
    <!-- A replikáció működéséhez, a rendszer tábla kiegészítése pk_id-val. (bugfix)         -->
""", """    <!-- =================================================================================== -->
    <!-- A telepítés alap paramétereinek beállítása..                                        -->
    <!-- =================================================================================== -->
    <include file="install-parameters.xml" relativeToChangelogFile="true"/>

    <!-- =================================================================================== -->
    <!-- A replikáció működéséhez, a rendszer tábla kiegészítése pk_id-val. (bugfix)         -->
""")
      out.write(text)

  out.close()
  os.remove(fname+'_old')


def sema_atszervezes(repos):
  def is_needed(repo):
    return os.path.isfile(base+db_path+'/install-parameters.xml') == False
  for repo in repos[0:]:
  # prepare
    base = 'c:/GIT/MLFF/'+repo+'/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    if not is_needed(repo): continue
    git_init(move_upper_dir(base))
    schema = get_schema(base, db_path)
    to_replace = [['core-customer', db],['core_customer', db_path], ['customer', schema]]

    print(repo)
    copy_file_and_replace(r'c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/install-parameters.xml', base+db_path+'/install-parameters.xml', to_replace)
    change_file(base+db_path+'/liquibase-install-step-01.xml')
    os.remove(base+db_path+'/_init_dbs/'+db_path+'-db-install-parameters.xml')
    os.remove(base+db_path+'/_init_dbs/'+db_path+'-db-install.xml')
    copy_file_and_replace('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/_init_dbs/core_customer-db-install.xml',
                          base+db_path+'/_init_dbs/'+db_path+'-db-install.xml', to_replace)
    shutil.rmtree(base+db_path+'/_init_dbs/'+db_path+'/'+schema)
    copy_dir('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/_init_dbs/core_customer/customer/',
             base+db_path+'/_init_dbs/'+db_path+'/'+schema)
    replace_in_file(base+db_path+'/_init_dbs/'+db_path+'/'+schema+'/service-user.sql', to_replace)
    copy_dir('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/customer/schema',
             base+db_path+'/'+'/'+schema+'/schema')
    path = base+db_path+'/'+schema
    replace_in_file(path+'/schema/create-schema.sql', to_replace)
    replace_in_file(path+'/schema/alter-service-user.sql', to_replace)
    replace_in_file(path+'/schema/create-roles.sql', to_replace)
    os.remove(path+'/create-schema.sql')
    shutil.rmtree(move_upper_dir(path) + '/all-modules')
    copy_dir('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/all-modules/', move_upper_dir(path) + '/all-modules')
    replace_in_file(move_upper_dir(path) + '/all-modules/functions/gen_create_table_statement.sql', to_replace)
    replace_in_file(move_upper_dir(path) + '/all-modules/functions/gen_hist_trigger_function.sql', to_replace)
    replace_in_file(move_upper_dir(path) + '/all-modules/procedures/hist_table_generator.sql', to_replace)
    replace_in_file(move_upper_dir(path) + '/all-modules/procedures/hist_trigger_generator.sql', to_replace)
    os.remove(base+db_path+'/liquibase-install-step-02.xml')
    copy_file_and_replace('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/liquibase-install-step-02.xml',
                          base+db_path+'/liquibase-install-step-02.xml', to_replace)
    os.remove(path+'/liquibase-install-schema.xml')
    copy_file_and_replace('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/customer/liquibase-install-schema.xml',
                          path+'/liquibase-install-schema.xml', to_replace)

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    repos = os.listdir(base)
    #repos = [x for x in os.listdir(base) if x.startswith('mlff-enforcement')]
    #repos = ['doc-postgredb']
    docker_image_hely_modositas(repos)
    sema_atszervezes(repos)
