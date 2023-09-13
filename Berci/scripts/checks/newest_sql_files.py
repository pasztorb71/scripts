import os
import re
import time

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
            if any([(x in l) for x in ['CREATE TABLE', 'ALTER TABLE', 'DROP TABLE']]) \
                    and not any([(x in l) for x in
                                 ['CONSTRAINT', '$hist', '_p_', 'REPLICA IDENTITY', 'OWNER TO', 'dbz_signal',
                                  'databasechangelog']]):
                out.append(l.lstrip())
    return out


def get_schema_xml_files_labels(lines: list[str]) -> list[str, str]:
    filelist = []
    for line in lines:
        m = re.match(".*(schema-version-.*.xml).*",line)
        if m:
           m_label = re.match('.*labels=.*,\s(.*)"/>.*', line)
           label = m_label.group(1) if m_label else None
           filelist.append([m.group(1), label])
    return filelist


def get_label_advanced(file, xml_files:list[str, str]):
    sql_file_name = file.rsplit('\\', 1)[1]
    for xml_f in xml_files:
        if not os.path.exists(file.rsplit('\\', 2)[0] + '/schema-version-0.xml'):
            return None
        try:
            lines = []
            schema_version_file = file.rsplit('\\', 2)[0] + f'/{xml_f[0]}'
            with open(schema_version_file, 'r', encoding='utf8') as f:
                for line in f.readlines():
                    if sql_file_name in line:
                        if xml_f[1]:
                            return xml_f[1]
                        else:
                            return
        except Exception as e:
            print(file)
            raise e


def get_label(file):
    file_name = file.rsplit('\\', 1)[1]
    if not os.path.exists(file.rsplit('\\', 2)[0] + '/schema-version-0.xml'):
        return None
    try:
        lines = []
        with open(file.rsplit('\\', 2)[0] + '/schema-version-0.xml', 'r', encoding='utf8') as f:
            lines = f.readlines()
            for line in lines:
                if file_name in line:
                    m = re.match('.*labels=.*,\s(.*)"/>.*', line)
                    return m.group(1) if m else None
            return get_label_advanced(file, get_schema_xml_files_labels(lines))
    except Exception as e:
        print(file)
        raise e


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


if __name__ == '__main__':
    prev_db_name = ''
    modtime = datetime.strptime('23/07/04 15:41:00', '%y/%m/%d %H:%M:%S')
    for file in utils_file.get_files_from_path_fname_filtered('c:/GIT/MLFF/', '.sql'):
        if 'ddl_changes_module' in file:
            continue
        if not file_modtime_greater(file, modtime):
            continue
        commands = get_important_commands_from_file(file)
        if not commands:
            continue
        db_name = utils_db.get_db_name(file)
        if db_name != prev_db_name:
            print('\n' + db_name)
            prev_db_name = db_name
        label = get_label(file)
        print(f"\tlabel:{label}, {file}")
        print('\t\t' + '\n\t\t'.join(commands))
