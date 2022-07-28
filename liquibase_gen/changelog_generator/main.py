import re

import utils
import version
from Repository import Repository
from liquibase_gen.changelog_generator.Ticket import Ticket
from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
from utils import get_files_from_path_ext_filtered


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
    if re.match('UPDATE.*', stmt) or re.match('DELETE FROM.*', stmt):
        print('COMMIT;')


if __name__ == '__main__':
    ticket = Ticket('MLFFDEV-4877')
    repo = Repository('psp-clearing')
    print('Repository name: ' + repo.get_name())
    version.check_schema_version_file(ticket.get_version(), repo)
    g = Changelog_header_generator(author='bertalan.pasztor',jira=ticket.name, version=ticket.get_version(), serial=1 )
    #commands = list(filter(None, load_from_file('C:/Users/bertalan.pasztor/Documents/MLFF/trip_segment.txt')))
    #TODO history táblára is megcsinálni
    commands = [
        "ALTER TABLE psp_clearing.psp_settlement_package ADD sent_at timestamptz(6) NULL;",
        "COMMENT ON COLUMN psp_clearing.psp_settlement_package.sent_at IS 'The time when a package is sent to the psp and the ACK arrived';",
        "ALTER TABLE psp_clearing.psp_settlement_package$hist ADD sent_at timestamptz(6) NULL;",
        "COMMENT ON COLUMN psp_clearing.psp_settlement_package$hist.sent_at IS 'Logged field: The time when a package is sent to the psp and the ACK arrived';",
    ]
    #TODO tasks = [new_enum('notification_wa.event.event', '')]
    try:
        for stmt in commands[0:]:
            header, tablename = g.generate_header(stmt)
            if tablename:
                version.check_table_version_file(ticket.get_version(), repo, tablename)
            if header:
                print()
                print(header[:-1])
            p_print(stmt)
            """
            if re.match('.*ADD CONSTRAINT .* CHECK ',stmt):
                table_name = utils.get_tablename_from_command(stmt)
                column_name = utils.get_columnname_from_command(stmt)
                stmt = "COMMENT ON COLUMN " + table_name + '.' + column_name + " IS 'komment';"
                header, tablename = g.generate_header(stmt)
                print()
                print(header[:-1])
                p_print(stmt)
            """
    except Exception as e:
        print(stmt)
        raise e