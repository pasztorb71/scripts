import re

import version
from Repository import Repository
from liquibase_gen.changelog_generator.Ticket import Ticket
from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
from utils import get_files_from_path_ext_filtered, get_tablename_from_command


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
                ]
    if any([re.match(pat, stmt) for pat in patterns]):
        return True
    return False

def gen_history_command_from_command(stmt):
    name = get_tablename_from_command(stmt)
    if re.match('COMMENT ON COLUMN.*',stmt):
        stmt = stmt.replace(" IS '", " IS 'Logged field: ")
    return f"{name}$hist".join(stmt.rsplit(name,1))



def process_commands():
    history_commands = []
    for stmt in commands[0:]:
        if is_history_related_command(stmt):
            history_commands.append(gen_history_command_from_command(stmt))
    try:
        for stmt in commands[0:] + history_commands:
            header, tablename = g.generate_header(stmt)

            if tablename:
                version.check_table_version_file(ticket.get_version(), repo, tablename) # DDL sql

            if header:
                print()
                print(header[:-1])
            else:
                if 'COMMENT ON COLUMN ' not in stmt:
                    raise Exception("No header found")
            p_print(stmt)

    except Exception as e:
        print(stmt)
        raise e


if __name__ == '__main__':
    ticket = Ticket('MLFFDEV-5309')
    repo = Repository('psp-clearing')
    print('Repository name: ' + repo.get_name())
    version.check_schema_version_file(ticket.get_version(), repo)
    g = Changelog_header_generator(author='bertalan.pasztor', jira=ticket.name, version=ticket.get_version(), serial=0)
    commands = [
        "ALTER TABLE psp_clearing.psp_correction ADD psp_settlement_batch_id varchar(30) NULL;",
        "COMMENT ON COLUMN psp_clearing.psp_correction.psp_settlement_batch_id IS 'Identifier of settlement batch record (x__id from the psp_clearing.psp_settlement_batch) (for conciliation)';",
        "ALTER TABLE psp_clearing.psp_correction ADD CONSTRAINT fk_pspcorr_pspsettbatch_id FOREIGN KEY (psp_settlement_batch_id) REFERENCES psp_clearing.psp_settlement_batch(x__id) DEFERRABLE",
        "CREATE INDEX ix_pspcorr_pspsettbatch_id ON psp_clearing.psp_correction USING btree (psp_settlement_batch_id);",

    ]
    # TODO tasks = [new_enum('notification_wa.event.event', '')]
    process_commands()