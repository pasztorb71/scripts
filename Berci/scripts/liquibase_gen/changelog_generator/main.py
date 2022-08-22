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
    ticket = Ticket('MLFFDEV-5066')
    repo = Repository('notification-dispacther')
    print('Repository name: ' + repo.get_name())
    version.check_schema_version_file(ticket.get_version(), repo)
    g = Changelog_header_generator(author='bertalan.pasztor', jira=ticket.name, version=ticket.get_version(), serial=0)
    commands = [
        "DROP TABLE notification_dispatcher.staging;",
        "ALTER SCHEMA notification_common RENAME TO notification_dispacther;",
        "DROP TABLE notification_dispatcher.staging;",
        "ALTER TABLE notification_dispacther.notification DROP CONSTRAINT ck_notif_event_name;",
        "DELETE FROM notification_dispacther.notification WHERE event_name NOT IN ('REGISTRATION','PHONE_NUMBER_MODIFICATION','AD_HOC_TICKET_PAYMENT_SUCCESS','AD_HOC_TICKET_PAYMENT_FAILED','TICKET_PAYMENT_SUCCES','TICKET_PAYMENT_FAILED','TRIP_PAYMENT_FAILED','TRIP_PAYMENT_SUCCESS','APPROACH_TOLL_ROAD_SEG','ENTER_CLOSED_SEG','EXIT_CLOSED_SEG','ENTER_OPEN_SEG');",
        "ALTER TABLE notification_dispacther.notification ADD CONSTRAINT ck_notif_event_name CHECK (((event_name)::text = ANY (ARRAY[('REGISTRATION'::character varying)::text, ('PHONE_NUMBER_MODIFICATION'::character varying)::text, ('AD_HOC_TICKET_PAYMENT_SUCCESS'::character varying)::text, ('AD_HOC_TICKET_PAYMENT_FAILED'::character varying)::text, ('TICKET_PAYMENT_SUCCES'::character varying)::text, ('TICKET_PAYMENT_FAILED'::character varying)::text, ('TRIP_PAYMENT_FAILED'::character varying)::text, ('TRIP_PAYMENT_SUCCESS'::character varying)::text, ('APPROACH_TOLL_ROAD_SEG'::character varying)::text, ('ENTER_TOLL_ROAD_SEG'::character varying)::text, ('EXIT_TOLL_ROAD_SEG'::character varying)::text])));",
        "COMMENT ON COLUMN notification_dispacther.notification.event_name IS 'event name for notification ENUM:''REGISTRATION'',''PHONE_NUMBER_MODIFICATION'',''AD_HOC_TICKET_PAYMENT_SUCCESS'',''AD_HOC_TICKET_PAYMENT_FAILED'',''TICKET_PAYMENT_SUCCES'',''TICKET_PAYMENT_FAILED'',''TRIP_PAYMENT_FAILED'',''TRIP_PAYMENT_SUCCESS'',''APPROACH_TOLL_ROAD_SEG'',''ENTER_CLOSED_SEG'',''EXIT_CLOSED_SEG'',''ENTER_OPEN_SEG''';",
        "COMMENT ON COLUMN notification_dispacther.notification$hist.event_name IS 'Logged field: event name for notification ENUM:''REGISTRATION'',''PHONE_NUMBER_MODIFICATION'',''AD_HOC_TICKET_PAYMENT_SUCCESS'',''AD_HOC_TICKET_PAYMENT_FAILED'',''TICKET_PAYMENT_SUCCES'',''TICKET_PAYMENT_FAILED'',''TRIP_PAYMENT_FAILED'',''TRIP_PAYMENT_SUCCESS'',''APPROACH_TOLL_ROAD_SEG'',''ENTER_CLOSED_SEG'',''EXIT_CLOSED_SEG'',''ENTER_OPEN_SEG''';",
    ]
    # TODO tasks = [new_enum('notification_wa.event.event', '')]
    process_commands()