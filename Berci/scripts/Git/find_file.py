from utils_file import get_files_from_path_ext_find_content

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    a = get_files_from_path_ext_find_content(base, '.sql', ' FOREIGN KEY ')
    print('\n'.join(a))