import os

from utils import git_init, move_upper_dir, copy_file_and_replace, create_old_file, \
  replace_in_file, get_files_from_path_ext_filtered, load_from_file
from Repository import get_schema, get_db_name


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
    return repo not in ['mlff-settlement-psp-clearing-postgredb', 'mlff-core-customer-postgredb']
  for repo in repos[0:]:
  # prepare
    base = 'c:/GIT/MLFF/'+repo+'/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    if not is_needed(repo): continue

    #git_init(move_upper_dir(base))
    schema = get_schema(base, db_path)
    to_replace = [['schema_name_'+schema, 'schema_name']]

    print(repo)
    path = base+db_path+'/'+schema+'/'
    any(replace_in_file(x, to_replace) for x in get_files_from_path_ext_filtered(path, '', ''))
    path = base+db_path+'/'+schema+'/tables/'
    any(replace_in_file(x, to_replace) for x in get_files_from_path_ext_filtered(path, '', ''))
    path = base+db_path+'/all-modules/'
    any(replace_in_file(x, to_replace) for x in get_files_from_path_ext_filtered(path, '', ''))

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    repos = load_from_file('repos.txt')
    #repos = [x for x in os.listdir(base) if x.startswith('mlff-enforcement')]
    repos = ['mlff-core-notification-wa-postgredb']
    sema_atszervezes(repos)
