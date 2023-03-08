import os
import time

import utils_db
import utils_file
from datetime import datetime

def mtime_to_datetime(mtime):
    convert_time = time.localtime(mtime)
    format_time = time.strftime('%d%m%Y %H:%M:%S', convert_time)
    return datetime.strptime(format_time, '%d%m%Y %H:%M:%S')


def get_commands_from_file(file):
    out = []
    with open(file, 'r') as f:
        for l in f.read().split('\n'):
            if any([(x in l) for x in ['CREATE TABLE', 'ALTER TABLE', 'DROP TABLE']])\
                    and not any([(x in l) for x in ['CONSTRAINT', '$hist', '_p_']]):
                out.append(l.lstrip())
    return out

if __name__ == '__main__':
    prev_db_name = ''
    v_time = datetime.strptime('02/16/23 11:22:00', '%m/%d/%y %H:%M:%S')
    files = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF/', '.sql')
    last_result= open('last_result.txt', 'a+')
    for file in files[0:]:
        if mtime_to_datetime(os.path.getmtime(file)) > v_time:
            commands = get_commands_from_file(file)
            if commands:
                db_name = utils_db.get_db_name(file)
                if db_name != prev_db_name:
                    print(utils_db.get_db_name(file))
                    prev_db_name = db_name
                print('\t' + '\n\t'.join(commands))
