import os
import re
import time

import Repository
from Git.Git_class import Git
from utils import utils_file, utils_db
from datetime import datetime


def mtime_to_datetime(mtime):
    convert_time = time.localtime(mtime)
    format_time = time.strftime('%d%m%Y %H:%M:%S', convert_time)
    return datetime.strptime(format_time, '%d%m%Y %H:%M:%S')


def get_important_commands_from_file(file):
    out = []
    if any([(x in file) for x in ['_all-modules']]):
        return out
    with open(file, 'r') as f:
        for l in f.read().split('\n'):
            if any([(x in l) for x in ['CREATE TABLE', 'ALTER TABLE', 'DROP TABLE', 'ADD COLUMN']]) \
                    and not any([(x in l) for x in
                                 ['CONSTRAINT', '$hist', '_p_', 'REPLICA IDENTITY', 'OWNER TO', 'dbz_signal',
                                  'databasechangelog', '|| tablename']]):
                out.append(l.lstrip())
    return out


def get_label_from_file(file):
    with open(file, 'r') as f:
        data = f.read()
    m = re.match('.*labels:(.*)\n--comment', data, re.DOTALL)
    if m:
        return m.group(1)
    return None


def get_modification_time(filename):
    f_arr = filename.split('\\liquibase')
    fname = 'liquibase' + f_arr[1].replace('\\', '/')
    repo = f_arr[0]
    command = f'cmd /u /c git -C {repo} log -1 --format="%ad" --date=format:"%Y-%m-%d %H:%M:%S" {fname}'
    date_str = os.popen(command).read().replace('\n','')
    if not date_str:
        date_str = '2999-01-01 00:00:00'
    try:
        a = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except Exception as e:
        print(f'{fname}: {date_str}')
        raise e
    return a


def file_modtime_greater(filename: str, mtime: datetime) -> bool:
    return get_modification_time(filename) > mtime


def is_file_needed(file, modtime):
    return any([x in file for x in
                ['ddl_changes_module',
                 '_all-modules',
                 'create-database',
                 '__init_dbs'
                ]
               ]) or not file_modtime_greater(file, modtime)


if __name__ == '__main__':
    prev_db_name = ''
    path = 'c:\\GIT\\MLFF\\'
    #path = path + '\\mlff-enforcement-detection-postgredb\\'
    modtime = datetime.strptime('24/02/00 17:00:00', '%y/%m/%d %H:%M:%S')
    for file in utils_file.get_files_from_path_fname_filtered(path, '.sql'):
        repo = Repository.Repository.get_repo_from_filename(file)
        git = Git(repo=repo.name)
        if is_file_needed(file, modtime):
            continue
        a = git.commits_on_file_on_branch(file, after=modtime)
        if not a.has_commits:
            continue
        if a.commitlist_include(message='MLFFSUP-6171'):
            continue
        commands = get_important_commands_from_file(file)
        if not commands:
            continue
        db_name = repo.dbname
        if db_name != prev_db_name:
            print('\n' + db_name)
            prev_db_name = db_name
        label = repo.get_release_label_release_of_file(file)
        print(f"\tlabel:{label}, {file}")
        print('\t\t' + '\n\t\t'.join(commands))
