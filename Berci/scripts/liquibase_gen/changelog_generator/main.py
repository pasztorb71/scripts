import re

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


def is_history_related_command(stmt):
    pass


def gen_history_command_from_command(stmt):
    pass


def process_commands():
    try:
        history_commands = []
        for stmt in commands[0:]:
            header, tablename = g.generate_header(stmt)
            # TODO MAke history handling
            """
            if utils.is_history_table(repo.get_db_name(), repo.get_schema(), tablename):
                header, hist_tablename = g.generate_header(stmt, hist=True)
                history_changesets.append(header[:-1])
                history_changesets.append(stmt)
            """
            if tablename:
                version.check_table_version_file(ticket.get_version(), repo, tablename) # DDL sql

            if is_history_related_command(stmt):
                history_commands.append(gen_history_command_from_command(stmt))

            if header:
                print()
                print(header[:-1])
            else:
                raise Exception("No header found")
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
    ticket = Ticket('MLFFDEV-5309')
    repo = Repository('psp-clearing')
    print('Repository name: ' + repo.get_name())
    version.check_schema_version_file(ticket.get_version(), repo)
    g = Changelog_header_generator(author='bertalan.pasztor', jira=ticket.name, version=ticket.get_version(), serial=0)
    # TODO history táblára is megcsinálni
    commands = [
        "ALTER TABLE psp_clearing.psp_correction ADD psp_settlement_batch_id varchar(30) NULL;",
        "COMMENT ON COLUMN psp_clearing.psp_correction.psp_settlement_batch_id IS 'Identifier of settlement batch record (x__id from the psp_clearing.psp_settlement_batch) (for conciliation)';",
        "ALTER TABLE psp_clearing.psp_correction ADD CONSTRAINT fk_pspcorr_pspsettbatch_id FOREIGN KEY (psp_settlement_batch_id) REFERENCES psp_clearing.psp_settlement_batch(x__id) DEFERRABLE",
        "CREATE INDEX ix_pspcorr_pspsettbatch_id ON psp_clearing.psp_correction USING btree (psp_settlement_batch_id);",
        "ALTER TABLE psp_clearing.psp_correction$hist ADD psp_settlement_batch_id varchar(30) NULL;",
        "COMMENT ON COLUMN psp_clearing.psp_correction$hist.psp_settlement_batch_id IS 'Logged field: Identifier of settlement batch record (x__id from the psp_clearing.psp_settlement_batch) (for conciliation)';",

    ]
    # TODO tasks = [new_enum('notification_wa.event.event', '')]
    process_commands()