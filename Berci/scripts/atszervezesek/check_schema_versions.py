import utils
import utils_file

if __name__ == '__main__':
    files = utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF', 'schema-version-0.xml')
    for file in files:
        print(file)
        with open(file, 'r', encoding='utf8') as f:
            for l in f.readlines():
                if 'alverzióhoz tartozó, sql tábla változások..' in l:
                    print(f'  ', l, end='')
