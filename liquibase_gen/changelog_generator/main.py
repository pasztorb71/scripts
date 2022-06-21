from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
from utils import get_files_from_path_ext_filtered

def get_commands():
    files = get_files_from_path_ext_filtered("c:/GIT/MLFF", '.sql', 'DDL')
    commands = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            for l in f.read().split('\n'):
                if l and not any(l.startswith(x) for x in ['--', 'COMMIT', 'call']):
                    commands.append(l)
    return commands

if __name__ == '__main__':
    commands = get_commands()
    g = Changelog_header_generator(author='bertalan.pasztor',jira='MLFFDEV-2355', version='0.3.0' )
    #commands = ['ALTER TABLE account_info.payment_method DROP COLUMN payment_method;']
    try:
        for stmt in commands[0:]:
            header = g.generate_header(stmt)
            print(header[:-1])
            print(stmt)
            print()
    except Exception as e:
        print(stmt)
        raise e