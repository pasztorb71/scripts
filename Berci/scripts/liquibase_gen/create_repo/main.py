import os
import re
import shutil

from utils import move_upper_dir, git_init
from utils_file import copy_dir, replace_in_file, copy_file, copy_file_and_replace


def create_version_file(fname):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write("""<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

    <!-- ============================================================================== -->
    <!-- Adott alverzióhoz tartozó, sql tábla változáskat gyűjtő xml leíró file..       -->
    <!-- ============================================================================== -->

    <!-- ============================================================================== -->

</databaseChangeLog>

    """)


def create_tables_file(fname):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write("""<databaseChangeLog xmlns="http://www.liquibase.org/xml/ns/dbchangelog"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.liquibase.org/xml/ns/dbchangelog
    http://www.liquibase.org/xml/ns/dbchangelog/dbchangelog-4.3.xsd">

    <!-- =================================================================================== -->
    <!-- A schema-hoz tartozó táblák létrehozása...                                          -->
    <!-- Részlegesen kötött sorrendben kell futtatni, a Foreign Key hivatkozások miatt!      -->
    <!-- =================================================================================== -->


</databaseChangeLog>
""")

if __name__ == '__main__':
    src_repo = 'mlff-core-customer-postgredb'
    src_base = 'c:/GIT/MLFF/'+src_repo
    src_db = re.match('.*mlff-(.*)-postgredb', src_base).group(1)
    src_db_path = src_db.replace('-', '_')
    src_schema = 'customer'
  #prepare
    repo = 'mlff-enforcement-eligibilty-declaration1-postgredb'
    base = 'c:/GIT/MLFF/'+repo
    db = re.match('.*mlff-(.*)-postgredb', base).group(1)
    db_path = db.replace('-', '_')
    schema = 'eligibilty_declaration1'
    version = '0.05.0'
    service_user = schema + '_service'
    to_replace = [[src_db, db],[src_db_path, db_path], [src_schema, schema]]
  #database
    git_init(base)
    os.makedirs(base+'/liquibase/'+db_path)
    src_path = src_base+'/liquibase/'+src_db_path
    path = base+'/liquibase/'+db_path+'/_init_dbs'
    copy_file_and_replace(src_base+'/README.adoc', base+'/README.adoc', to_replace)
    copy_dir(src_base+'/liquibase/'+src_db_path+'/_init_dbs', path)
    os.rename(path+'/'+src_db_path, path+'/'+db_path)
    os.rename(path+'/'+src_db_path+'-db-install.xml', path+'/'+db_path+'-db-install.xml')
    replace_in_file(path+'/'+db_path+'-db-install.xml', to_replace)
    copy_file_and_replace(src_path+'/install-parameters.xml', move_upper_dir(path)+'/install-parameters.xml', to_replace)
    os.rename(path+'/'+db_path+'/'+src_schema, path+'/'+db_path+'/'+schema)
    replace_in_file(path+'/'+db_path+'/create-database.sql', to_replace)
    replace_in_file(path+'/'+db_path+'/'+schema+'/service-user.sql', to_replace)
    copy_dir(src_path+'/all-modules', move_upper_dir(path)+'/all-modules')
    path = move_upper_dir(path)+'/all-modules/'
    replace_in_file(path+'functions/gen_create_table_statement.sql', to_replace)
    replace_in_file(path+'functions/gen_hist_trigger_function.sql', to_replace)
    replace_in_file(path+'procedures/hist_table_generator.sql', to_replace)
    replace_in_file(path+'procedures/hist_trigger_generator.sql', to_replace)
    copy_file_and_replace(src_path+'/liquibase-install-step-01.xml', move_upper_dir(path)+'/liquibase-install-step-01.xml', to_replace)
    copy_file_and_replace(src_path+'/liquibase-install-step-02.xml', move_upper_dir(path)+'/liquibase-install-step-02.xml', to_replace)
    copy_dir(src_path+'/'+src_schema, move_upper_dir(path)+'/'+schema)
    path = move_upper_dir(path)+'/'+schema
    replace_in_file(path+'/schema/create-schema.sql', to_replace)
    replace_in_file(path+'/schema/alter-service-user.sql', to_replace)
    replace_in_file(path+'/schema/create-roles.sql', to_replace)
    create_version_file(path+'/xml-version-tree/version-0/'+version+'.xml')
    os.remove(path+'/xml-version-tree/version-0/0.02.0.xml')
    shutil.rmtree(path+'/tables')
    os.makedirs(path+'/tables')
    create_tables_file(path+'/tables/create-tables.xml')
    replace_in_file(path+'/liquibase-install-schema.xml', to_replace)
    replace_in_file(path+'/xml-version-tree/schema-version-0.xml', [['0.02.0', version]])
