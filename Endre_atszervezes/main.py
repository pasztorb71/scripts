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

def move_file(src, dst):
    print('file: '+src, dst)
    if os.path.isfile(src):
        print('  '+src)
        shutil.move(src, dst)

def move_up(path):
    return path.rsplit('/',1)[0] if path[-1] != '/' else path.rsplit('/',2)[0]

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/mlff-core-vehicle-postgredb másolata/liquibase/'
    db = re.match('.*mlff-(.*)-postgredb', base).group(1)
    db_path = db.replace('-', '_')
    copy_dir(base+'_init_dbs', base+'_init_dbs_copy')
    schema = get_schema()
    move_dir(base+'_init_dbs', base+db_path+'/_init_dbs')
    move_file(base+'liquibase-install-databases.xml', base+db_path+'/liquibase-install-step-01.xml')
    move_file(base+'liquibase-install-'+db_path+'.xml', base+db_path+'/liquibase-install-step-02.xml')
    os.rename(base+db_path+'/_init_dbs/'+db_path+'/'+db_path+'-database.sql', base+db_path+'/_init_dbs/'+db_path+'/create-database.sql')
