import re

from liquibase_gen.changelog_generator.Ticket import Ticket
from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
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
    if re.match('UPDATE.*', stmt) or re.match('DELETE FROM.*', stmt):
        print('COMMIT;')


def check_version_file(ticket, repo):
    pass


if __name__ == '__main__':
    #commands = get_commands()
    ticket = Ticket('MLFFDEV-4603')
    #TODO létregozni DDL fájlt, ha kell és nem létezik
    #check_version_file(ticket.get_version(),Repository('psp-proxy'))
    #DDL fájl vége
    g = Changelog_header_generator(author='bertalan.pasztor',jira=ticket.name, version=ticket.get_version(), serial=1 )
    #commands = list(filter(None, load_from_file('C:/Users/bertalan.pasztor/Documents/MLFF/trip_segment.txt')))
    #TODO új enum hozzáadását komplett feladatként felvenni
    commands = [
        "ALTER TABLE notification_wa.event DROP CONSTRAINT ck_event_event;",
        "DELETE FROM notification_wa.event WHERE event NOT IN('REGISTRATION', 'PHONE_NUMBER_MODIFICATION', 'AD_HOC_TICKET_PAYMENT_SUCCESS', 'AD_HOC_TICKET_PAYMENT_FAILED', 'TICKET_PAYMENT_SUCCES', 'TICKET_PAYMENT_FAILED', 'TRIP_PAYMENT_FAILED', 'TRIP_PAYMENT_SUCCESS', 'APPROACH_TOLL_ROAD_SEG', 'ENTER_CLOSED_SEG', 'EXIT_CLOSED_SEG', 'ENTER_OPEN_SEG');",
        "ALTER TABLE notification_wa.event ADD CONSTRAINT ck_event_event CHECK (((event)::text = ANY ((ARRAY['REGISTRATION'::character varying, 'PHONE_NUMBER_MODIFICATION'::character varying, 'AD_HOC_TICKET_PAYMENT_SUCCESS'::character varying, 'AD_HOC_TICKET_PAYMENT_FAILED'::character varying, 'TICKET_PAYMENT_SUCCES'::character varying, 'TICKET_PAYMENT_FAILED'::character varying, 'TRIP_PAYMENT_FAILED'::character varying, 'TRIP_PAYMENT_SUCCESS'::character varying, 'APPROACH_TOLL_ROAD_SEG'::character varying, 'ENTER_CLOSED_SEG'::character varying, 'EXIT_CLOSED_SEG'::character varying, 'ENTER_OPEN_SEG'::character varying])::text[])));",
        "COMMENT ON COLUMN notification_wa.event.event IS 'event name for notification ENUM:''REGISTRATION'',''PHONE_NUMBER_MODIFICATION'',''AD_HOC_TICKET_PAYMENT_SUCCESS'',''AD_HOC_TICKET_PAYMENT_FAILED'',''TICKET_PAYMENT_SUCCES'',''TICKET_PAYMENT_FAILED'',''TRIP_PAYMENT_FAILED'',''TRIP_PAYMENT_SUCCESS'',''APPROACH_TOLL_ROAD_SEG'',''ENTER_CLOSED_SEG'',''EXIT_CLOSED_SEG'',''ENTER_OPEN_SEG''';"
    ]
    try:
        for stmt in commands[0:]:
            header = g.generate_header(stmt)
            print(header[:-1])
            p_print(stmt)
            print()
    except Exception as e:
        print(stmt)
        raise e