import re

import utils
import utils_file

if __name__ == '__main__':
    files = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF', '-DDL-000.sql')
    for file in files[0:]:
        print(file)
        #utils.git_init_from_path(file)
        #continue
        with open(file, 'r', encoding='utf8') as f:
            lines = f.readlines()
            out = []
            for l in lines:
                m = re.match('--changeset endre.balazs:(.*) runOnChange:true', l)
                if m:
                    if not any(x in m.group(1) for x in ['MLFFDEV-', '-DDL-']):
                        print(f'  {l}', end='')
                        l = l.replace(m.group(1), f'{m.group(1)}-DDL-MLFFDEV-8134-01')
                    if 'MLFFDEV-' in l:
                        print(f'Kivétel: {m.group(1)}')
                out.append(l)
        with open(file, 'w', encoding='utf8') as f:
            f.writelines(out)