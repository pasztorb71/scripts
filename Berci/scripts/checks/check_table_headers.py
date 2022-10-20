import re

import utils

if __name__ == '__main__':
    files = utils.get_files_from_path_fname_filtered('c:/GIT/MLFF', '-DDL-000.sql')
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
