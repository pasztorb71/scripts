import os
import re

from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
from liquibase_gen.changelog_generator.version_call import Version_call
from utils import get_files_from_path_ext_filtered,load_from_file,get_schema_from_command


def get_commands():
    files = get_files_from_path_ext_filtered("c:/GIT/MLFF", '.sql', 'DDL')
    commands = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            for l in f.read().split('/n'):
                if l and not any(l.startswith(x) for x in ['--', 'COMMIT', 'call']):
                    commands.append(l)
    return commands


def p_print(stmt):
    print(stmt)
    if re.match('UPDATE.*', stmt):
        print('COMMIT;')


if __name__ == '__main__':
    #commands = get_commands()
    version = '0.04.0'
    #TODO serial automatikus növelése
    #TODO jira olvasása
    g = Changelog_header_generator(author='bertalan.pasztor',jira='MLFFDEV-3858', version=version, serial=1 )
    commands = list(filter(None, load_from_file('C:/Users/bertalan.pasztor/Documents/MLFF/trip_segment.txt')))
    #commands = ["COMMENT ON TABLE vehicle.toll_category IS 'This table describes the toll category itself.';"]
    vc = Version_call(version, get_schema_from_command(commands[0]))
    try:
        for stmt in commands[0:]:
            header = g.generate_header(stmt)
            print(header[:-1])
            p_print(stmt)
            print()
    except Exception as e:
        print(stmt)
        raise e