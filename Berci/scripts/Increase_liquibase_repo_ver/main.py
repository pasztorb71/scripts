import glob

if __name__ == '__main__':
    old_ver = '0.4.1'
    new_ver = '0.6.0'
    files = list(glob.glob('c:/GIT/MLFF/*/etc/release/docker-compose.yml'))
    for file in files[0:]:
        out = []
        print(file)
        with open(file, 'r', encoding='utf8') as f:
            for line in f.readlines():
                if f'liquibase:{old_ver}' in line:
                    if line.startswith('#'):
                        continue
                    line = line.replace(f'liquibase:{old_ver}', f'liquibase:{new_ver}')
                out.append(line)
        with open(file, 'w', encoding='utf8') as f:
            f.writelines(out)