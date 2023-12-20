from utils.utils_file import get_files_from_path_ext_filtered

if __name__ == '__main__':
    sum = 0
    files = get_files_from_path_ext_filtered('c:/Users/bertalan.pasztor/PycharmProjects/liquibase/Berci/scripts/', '.py')
    print(f'fájlok száma: {len(files)}')
    for file in files:
        with open(file, encoding='utf8') as f:
            sum = sum + len(f.readlines())
    print(f'Sorok száma: {sum}')