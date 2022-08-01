import re

import utils
import version
from Repository import Repository
from liquibase_gen.changelog_generator.Ticket import Ticket
from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
from utils import get_files_from_path_ext_filtered


def get_commands():
    files = get_files_from_path_ext_filtered("c:/GIT/MLFF", '.sql', 'DDL')
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


def process_commands():
    try:
        history_changesets = []
        for stmt in commands[0:]:
            header, tablename = g.generate_header(stmt)
            # TODO MMAke history handling
            """
            if utils.is_history_table(repo.get_db_name(), repo.get_schema(), tablename):
                header, hist_tablename = g.generate_header(stmt, hist=True)
                history_changesets.append(header[:-1])
                history_changesets.append(stmt)
            """
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


if __name__ == '__main__':
    ticket = Ticket('MLFFDEV-4097')
    repo = Repository('tro-clearing')
    print('Repository name: ' + repo.get_name())
    version.check_schema_version_file(ticket.get_version(), repo)
    g = Changelog_header_generator(author='bertalan.pasztor', jira=ticket.name, version=ticket.get_version(), serial=1)
    # commands = list(filter(None, load_from_file('C:/Users/bertalan.pasztor/Documents/MLFF/trip_segment.txt')))
    # TODO history táblára is megcsinálni
    commands = [
        "ALTER TABLE tro_clearing.ctsp_service_fee_share ADD CONSTRAINT fk_ctspserfeesh_segment_fee_id FOREIGN KEY (ctsp_service_fee_id) REFERENCES tro_clearing.ctsp_service_fee(x__id) DEFERRABLE;",
    ]
    # TODO tasks = [new_enum('notification_wa.event.event', '')]
    process_commands()