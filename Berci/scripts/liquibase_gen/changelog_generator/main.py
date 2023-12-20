import re

from utils import utils_command
import version
from Repository import Repository
from Ticket import Ticket
from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
from liquibase_gen.changelog_generator.commands import command_list
from liquibase_gen.changelog_generator.paramsfile import params
from utils.utils_command import get_tablename_from_command
from utils.utils_file import get_files_from_path_ext_and_cont_filtered


def get_commands():
    files = get_files_from_path_ext_and_cont_filtered("c:/GIT/MLFF", '.sql', 'DDL')
    # noinspection PyShadowingNames
    commands = []
    for file in files:
        with open(file, 'r', encoding='utf-8') as f:
            for line in f.read().split('/n'):
                if line and not any(line.startswith(x) for x in ['--', 'COMMIT', 'call']):
                    commands.append(line)
    return commands


def p_print(stmt):
    print(stmt)
    if re.match('UPDATE.*', stmt) or re.match('DELETE FROM.*', stmt):
        print('COMMIT;')


def is_history_related_command(stmt):
    if ' CONSTRAINT ' in stmt:
        return False
    patterns = ['.*ADD COLUMN.*',
                'COMMENT ON COLUMN.*',
                'COMMENT ON TABLE.*',
                '.*ALTER COLUMN.* TYPE ',
                '.*RENAME COLUMN.*',
                'DROP TABLE.*',
                '.* ADD .*',
                '.* DROP COLUMN .*',
                'ALTER TABLE .* RENAME TO .*',
                ]
    if any([re.match(pat, stmt) for pat in patterns]):
        return True
    return False

def gen_history_command_from_command(repo, stmt):
    stmt = stmt.replace("NOT NULL", "NULL")
    name = get_tablename_from_command(repo, stmt)
    if re.match('COMMENT ON COLUMN.*',stmt):
        stmt = stmt.replace(" IS '", " IS 'Logged field: ")
    return f"{name}$hist".join(stmt.rsplit(f'{name}',1))

def process_commands(repo):
    history_commands = []
    history_comm = False
    last_table = ''
    for stmt in commands[0:]:
        if is_history_related_command(stmt):
            a = gen_history_command_from_command(repo, stmt)
            history_commands.append(gen_history_command_from_command(stmt))
    try:
        for stmt in commands[0:] + history_commands:
            if g.is_newtable(utils_command.get_tablename_from_command(repo, stmt)) and '$hist' in g.prev_table:
                print(g.generate_trigger_section())
            header, tablename = g.generate_header(repo, stmt)

            if tablename:
                version.check_table_version_file(ticket.get_version(), repo, tablename) # DDL sql

            if header:
                print()
                print(header[:-1])
            else:
                if 'COMMENT ON COLUMN ' not in stmt:
                    raise Exception("No header found")
            p_print(f'{stmt};')
            history_comm = '$hist' in tablename
            last_table = tablename


    except Exception as e:
        print(stmt)
        raise e
    if history_comm:
        a = g.generate_trigger_section()
        print(a)

def process_commands_new(repo, version1):
    history_commands = []
    history_comm = False
    last_table = ''
    is_header = False
    for stmt in commands[0:]:
        pass
        if is_history_related_command(stmt):
            history_commands.append(gen_history_command_from_command(repo, stmt))
    try:
        for stmt in commands[0:] + history_commands:
            is_newtable = g.is_newtable(utils_command.get_tablename_from_command(repo, stmt))
            if is_newtable and '$hist' in g.prev_table:
                print(g.generate_trigger_section())
            header, tablename = g.generate_header(repo, stmt)
            if header:
                new_header = g.gen_new_header_from_old(header, tablename)
                cmd_block = g.generate_commandblock(header, stmt, tablename)
            else:
                cmd_block = stmt;

            #if tablename:
                #TODO check_schema_version_file
                #version.check_schema_version_file(version1, repo) #
                #version.check_table_version_file(version1, repo, tablename) # DDL sql

            if header and not is_header:
                print()
                print(new_header)
                is_header = True
            p_print(f'{cmd_block}')
            history_comm = '$hist' in tablename
            last_table = tablename
        print(block_end)


    except Exception as e:
        print(stmt)
        raise e
    if history_comm:
        a = g.generate_trigger_section()
        print(a)

block_end = """END$$;
COMMIT;
/\n"""

if __name__ == '__main__':
    ticket = Ticket('MLFFDEV-9595')
    repo = Repository(params['repository'], params['schema'])
    print('Repository name: ' + repo.get_name())
    version1 = ticket.get_version()
    g = Changelog_header_generator(author='bertalan.pasztor', jira=ticket.name, version=version1, serial=0)
    commands = command_list(repo)[0].replace('\n','').split(';')
    #process_commands(repo)
    process_commands_new(repo, version1)

