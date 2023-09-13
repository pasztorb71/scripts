import re

from utils import utils_file, utils


def ddl_file_name_not_match_v_table_name():
    """Azokat a DDL fájlokat adja vissza, ahol a táblanév a DDL fájl nevéből
    nem egyezik a DDL fájlban hivatkozott táblanévvel a v_table_name változóban"""
    print(utils.whoami())
    files = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF/', '-DDL-')
    for file in files:
        if '\\save\\' in file:
            continue
        with open(file, 'r', encoding='utf8') as f:
            table_from_file = file.rsplit('\\', 1)[1].split('-', 1)[0]
            for line in f.readlines():
                if 'v_table_name  text :=' in line:
                    v_table_name = re.match(".*'(.*)';", line).group(1).replace('$hist','')
                    if v_table_name != table_from_file:
                        print(file)
                        print(f"  {line}", end='')


def schemaname_in_comments():
    """Azt nézi, hogy as sémanév benne van -e a COMMENT parancsban"""
    print(utils.whoami())
    files_tmp = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF/', '-DDL-')
    files = [f for f in files_tmp if '\\save\\' not in f]
    prev_file = ''
    for file in files:
        #if not any(x in file for x in ['0.08.0', '0.09.0']):
        #    continue
        with open(file, 'r', encoding='utf8') as f:
            for line in f.readlines():
                if 'COMMENT ON COLUMN' in line:
                        name = re.match('.*COMMENT ON COLUMN (.*) IS ', line).group(1)
                        if 'COMMENT ON COLUMN public.' not in line and len(name.split('.')) != 2:
                            if file != prev_file:
                                print(file)
                                prev_file = file
                            a = name.split('.')
                            b = len(name.split('.'))
                            print(f"  {name.ljust(60)}{line.lstrip()}", end='')

def check_table_creator_changeset_ids():
    """Azt ellenőrzi, hogy az ID megfelel -e az alábbi konvenciónak:
    <táblanév>-TBL-MLFFDEV-<ticket>-01"""
    print(utils.whoami())
    files = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF', '-TBL-000.sql')
    for file in files[0:]:
        with open(file, 'r', encoding='utf8') as f:
            lines = f.readlines()
            out = []
            for l in lines:
                m = re.match('--changeset .*:(.*) runOnChange:true', l)
                if m:
                    m1 = re.match('.*-DDL-MLFFDEV-[0-9]{4}-[0-9]{2}.*', l)
                    if not m1:
                        print(file)
                        print(m.group(1))


def check_table_creator_searchpaths():
    """Kiírja azokat a szkripteket amelyekben nem szerepel a SEARCH_PATH beállítás"""
    print(utils.whoami())
    files = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF', '-DDL-000.sql')
    for file in files[0:]:
        with open(file, 'r', encoding='utf8') as f:
            if 'SET search_path = ${schema_name};' not in f.read().split('\n'):
                print(file)


if __name__ == '__main__':
    ddl_file_name_not_match_v_table_name()
    #schemaname_in_comments()
    check_table_creator_changeset_ids()
    check_table_creator_searchpaths()

