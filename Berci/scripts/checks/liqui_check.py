import glob
import os
import re

import utils


def ddl_file_v_table_name():
    files = utils.get_files_from_path_fname_filtered('c:/GIT/MLFF/', '-DDL-')
    for file in files:
        with open(file, 'r', encoding='utf8') as f:
            table_from_file = file.rsplit('\\', 1)[1].split('-', 1)[0]
            for line in f.readlines():
                if 'v_table_name  text :=' in line:
                    v_table_name = re.match(".*'(.*)';", line).group(1).replace('$hist','')
                    if v_table_name != table_from_file:
                        print(file)
                        print(f"  {line}", end='')


def tablename_in_comments():
    files = utils.get_files_from_path_fname_filtered('c:/GIT/MLFF/', '-DDL-')
    for file in files:
        if not any(x in file for x in ['0.08.0', '0.09.0']):
            continue
        with open(file, 'r', encoding='utf8') as f:
            #print(file)
            for line in f.readlines():
                if 'COMMENT ON COLUMN' in line:
                        name = re.match('.*COMMENT ON COLUMN (.*) IS ', line).group(1)
                        if 'COMMENT ON COLUMN public.' not in line and len(name.split('.')) != 2:
                            a = name.split('.')
                            b = len(name.split('.'))
                            print(f"{name.ljust(60)}{line.lstrip()}", end='')


if __name__ == '__main__':
    #ddl_file_v_table_name()
    tablename_in_comments()