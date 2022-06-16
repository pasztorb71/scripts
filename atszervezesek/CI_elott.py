import os
import re

from utils import move_upper_dir, move_file, move_dir, create_old_file, get_db_name, get_schema


def change_file(fname):
    create_old_file(fname)
    out = open(fname, 'w', encoding='utf-8')
    if 'liquibase-install-step-' in fname:
        with open(fname+'_old', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                #modules
                is_row = re.match('.*<include file="(.*)all-modules/tables/databasechangelog', line)
                if is_row:
                    line = line.replace(is_row.group(1), '')
                #schema
                is_row = re.match('.*<include file="(_init_dbs/'+db_path+'/'+schema+'/'+schema+'-schema.sql)', line)
                if is_row:
                    line = line.replace(is_row.group(1), schema+'/liquibase-install-schema.xml')
                #delete row
                is_row = re.match('.*<include file="'+db_path+'/liquibase-'+schema+'.xml', line)
                if is_row:
                    line = ''
                out.write(line)
    elif '-db-install.xml' in fname:
        with open(fname+'_old', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                #database.sql
                is_row = re.match('.*<include file="'+db_path+'(/.*)-database.sql" relativeToChangelogFile="true"/>', line)
                if is_row:
                    line = line.replace(is_row.group(1), '/create')
                #schema-roles
                is_row = re.match('.*<include file="'+db_path+'/'+schema+'/(.*)schema-roles.sql" relativeToChangelogFile="true"/>', line)
                if is_row:
                    line = line.replace(is_row.group(1), '')
                #service-user
                is_row = re.match('.*<include file="'+db_path+'/'+schema+'/(.*)service-user.sql" relativeToChangelogFile="true"/>', line)
                if is_row:
                    line = line.replace(is_row.group(1), '')
                out.write(line)
    elif 'liquibase-install-schema.xml' in fname:
        with open(fname+'_old', 'r', encoding='utf-8') as f:
            text = f.read()
            text = text.replace("""    <!-- ============================================================================== -->
    <!-- A közös, azonos szerkezetű objektumok becsatolása..                            -->""",
                         """    <!-- ============================================================================== -->
    <!-- A schema létrehozása..                                                         -->
    <!-- ============================================================================== -->
    <include file="create-schema.sql" relativeToChangelogFile="true"/>
    
	<!-- ============================================================================== -->
    <!-- A közös, azonos szerkezetű objektumok becsatolása..                            -->""")\
            .replace(schema+'/install-modules.xml', 'install-modules.xml')\
            .replace(schema+'/tables/create-tables.xml', 'tables/create-tables.xml')\
            .replace(schema+'/liquibase-versions.xml', 'schema-versions.xml')\
            .replace(schema+'/install-dmls.xml', 'install-dmls.xml')
            out.write(text)
    elif 'README.md' in fname:
        with open(fname + '_old', 'r', encoding='utf-8') as f:
            text = f.read()
            text = text.replace('liquibase-install-databases.xml', db_path+'/liquibase-install-step-01.xml') \
            .replace('liquibase-install-'+db_path+'.xml', db_path+'/liquibase-install-step-02.xml')
            out.write(text)

    out.close()
    os.remove(fname + '_old')


if __name__ == '__main__':
    repo = 'doc-postgredb'
  #prepare
    base = 'c:/GIT/MLFF/'+repo+'/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    schema = get_schema(base, db_path)
  #database
    change_file(move_upper_dir(base) + '/README.md')
    move_dir(base + '_init_dbs', base + db_path + '/_init_dbs')
    move_file(base + 'liquibase-install-databases.xml', base + db_path + '/liquibase-install-step-01.xml')
    move_file(base + 'liquibase-install-' + db_path + '.xml', base + db_path + '/liquibase-install-step-02.xml')
    move_file(base + db_path + '/_init_dbs/' + db_path + '/' + db_path + '-database.sql', base + db_path + '/_init_dbs/' + db_path + '/create-database.sql')
    change_file(base+db_path+'/liquibase-install-step-01.xml')
    change_file(base+db_path+'/liquibase-install-step-02.xml')
    change_file(base+db_path+'/_init_dbs/' + db_path + '-db-install.xml')
    tmp = base+db_path+'/_init_dbs/'+db_path+'/'+schema
    move_file(tmp + '/' + schema + '-schema-roles.sql', tmp + '/schema-roles.sql')
    move_file(tmp + '/' + schema + '_service-user.sql', tmp + '/service-user.sql')
    move_file(tmp + '/' + schema + '-schema.sql', base + db_path + '/' + schema + '/create-schema.sql')
    change_file(base+db_path+'/_init_dbs/' + db_path + '-db-install.xml')
  #schema
    new_schema_path = base+db_path+'/'+schema+'/liquibase-install-schema.xml'
    move_file(base + db_path + '/liquibase-' + schema + '.xml', new_schema_path)
    change_file(new_schema_path)
    move_file(base + db_path + '/' + schema + '/liquibase-versions.xml', base + db_path + '/' + schema + '/schema-versions.xml')
