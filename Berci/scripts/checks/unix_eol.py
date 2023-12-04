import glob, os

from utils.utils_file import get_files_from_path_fname_filtered

for file in get_files_from_path_fname_filtered('c:/GIT/MLFF/', '.sh'):
    with open(file, 'r') as f:
        c = f.readline()
        if f.newlines == '\r\n':
            print(file)