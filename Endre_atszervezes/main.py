import os
import re
import shutil

from setuptools._distutils.dir_util import copy_tree


def get_schema():
    with open(base+'_init_dbs_copy/' + db_path + '-db-install-parameters.xml', 'r', encoding='utf-8') as f:
        text = f.read()
    return re.match('.*property name="schema_name_.*value="(.*)"/>', text, flags=re.DOTALL|re.MULTILINE).group(1)


def copy_dir(src, dst):
    if os.path.isdir(src):
        copy_tree(src, dst)


def move_dir(src, dst):
    print('dir : '+src, dst)
    if os.path.isdir(src):
        print('  '+src)
        shutil.move(src, dst)

def copy_file(src, dst):
    print('file: '+src, dst)
    if os.path.isfile(src):
        print('  '+src)
        shutil.copyfile(src, dst)

def move_file(src, dst):
    print('file: '+src, dst)
    if os.path.isfile(src):
        print('  '+src)
        shutil.move(src, dst)

def move_up(path):
    return path.rsplit('/',1)[0] if path[-1] != '/' else path.rsplit('/',2)[0]


def change_file(fname):
    if os.path.isfile(fname+'_old'):
        print('már létezik: ' + fname+'_old')
        #os.remove(fname)
        #move_file(fname + '_old', fname)
        return
    move_file(fname, fname+'_old')
    out = open(fname, 'w', encoding='utf-8')
    if 'liquibase-install-step-01.xml' in fname:
        with open(fname+'_old', 'r', encoding='utf-8') as f:
            for line in f.readlines():
                is_row = re.match('.*<include file="(.*)all-modules/tables/databasechangelog', line)
                if is_row:
                    line = line.replace(is_row.group(1), '')
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
    out.close()
    os.remove(fname + '_old')

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/mlff-core-vehicle-postgredb másolata/liquibase/'
    db = re.match('.*mlff-(.*)-postgredb', base).group(1)
    db_path = db.replace('-', '_')
    copy_dir(base+'_init_dbs', base+'_init_dbs_copy')
    schema = get_schema()
    move_dir(base+'_init_dbs', base+db_path+'/_init_dbs')
    move_file(base+'liquibase-install-databases.xml', base+db_path+'/liquibase-install-step-01.xml')
    move_file(base+'liquibase-install-'+db_path+'.xml', base+db_path+'/liquibase-install-step-02.xml')
    move_file(base+db_path+'/_init_dbs/'+db_path+'/'+db_path+'-database.sql', base+db_path+'/_init_dbs/'+db_path+'/create-database.sql')
    change_file(base+db_path+'/liquibase-install-step-01.xml')
    change_file(base+db_path+'/_init_dbs/' + db_path + '-db-install.xml')
    tmp = base+db_path+'/_init_dbs/'+db_path+'/'+schema
    move_file(tmp+'/'+schema+'-schema-roles.sql', tmp+'/schema-roles.sql')
    move_file(tmp+'/'+schema+'_service-user.sql', tmp+'/service-user.sql')
    move_file(tmp+'/'+schema+'-schema.sql', base+db_path+'/'+schema+'/create-schema.sql')
    change_file(base+db_path+'/_init_dbs/' + db_path + '-db-install.xml')
