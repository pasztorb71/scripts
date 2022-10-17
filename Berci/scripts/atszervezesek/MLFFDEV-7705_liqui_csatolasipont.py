import os

import utils

if __name__ == '__main__':
    from1 = '--changeLogFile=liquibase-install-db1-step-01.xml'
    from2 = '--changeLogFile=liquibase-install-db1-step-02.xml'
    for path, currentDirectory, files in os.walk('c:/GIT/MLFF/doc-postgredb'):
        repo = path.split('/')[3]
        dbname = utils.get_dbname_from_project(repo) if repo != 'doc-postgredb' else 'document'
        to1 = f'--changeLogFile={dbname}/liquibase-install-db1-step-01.xml'
        to2 = f'--changeLogFile={dbname}/liquibase-install-db1-step-02.xml'
        for file1 in files:
            if '.git' in path or '.git' in file1:
                continue
            out = []
            file = os.path.join(path, file1)
            with open(file, 'r', encoding='utf8') as f:
                for line in f.readlines():
                    if from1 in line:
                        line = line.replace(from1, to1)
                    if from2 in line:
                        line = line.replace(from2, to2)
                    out.append(line)
            with open(file, 'w', encoding='utf8') as f:
                f.writelines(out)