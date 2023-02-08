import os
import time

import utils_file
from datetime import datetime

def mtime_to_datetime(mtime):
    convert_time = time.localtime(mtime)
    format_time = time.strftime('%d%m%Y %H:%M:%S', convert_time)
    return datetime.strptime(format_time, '%d%m%Y %H:%M:%S')

if __name__ == '__main__':
    v_time = datetime.strptime('02/06/23 11:52:0', '%m/%d/%y %H:%M:%S')
    files = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF/', '.sql')
    for file in files[0:]:
        if mtime_to_datetime(os.path.getmtime(file)) > v_time:
            print(file)
