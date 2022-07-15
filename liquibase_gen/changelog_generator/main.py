import json
import os
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
    ticket = Ticket('MLFFDEV-4498')
    #TODO létregozni DDL fájlt, ha kell és nem létezik
    check_version_file(ticket.get_version(),'mlff-payment-psp-proxy-postgredb')
    #DDL fájl vége
    g = Changelog_header_generator(author='bertalan.pasztor',jira=ticket.name, version=ticket.get_version(), serial=1 )
    #commands = list(filter(None, load_from_file('C:/Users/bertalan.pasztor/Documents/MLFF/trip_segment.txt')))
    #TODO új enum hozzáadását komplett feladatként felvenni
    commands = [
        "ALTER TABLE psp_proxy.psp_data_assignment ALTER COLUMN psp_transaction_id DROP NOT NULL;",
        "UPDATE psp_proxy.psp_data_assignment SET psp_type = 'GOPAY';",
        "ALTER TABLE psp_proxy.psp_data_assignment ADD CONSTRAINT ck_pspdatass_psp_type CHECK (((psp_type)::text = ANY (ARRAY[('GOPAY'::character varying)::text, ('FELLO'::character varying)::text])));",
        "COMMENT ON COLUMN psp_proxy.psp_data_assignment.psp_type IS 'Identifier of the Payment Service Provider. Possible values: ''GOPAY'', ''FELLO''';"
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