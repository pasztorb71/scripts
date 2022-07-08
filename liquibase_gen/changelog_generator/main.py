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
    if re.match('UPDATE.*', stmt):
        print('COMMIT;')


if __name__ == '__main__':
    #commands = get_commands()
    ticket = Ticket('MLFFDEV-4353')
    #TODO létregozni DDL fájlt, ha kell és nem létezik
    g = Changelog_header_generator(author='bertalan.pasztor',jira=ticket.name, version=ticket.get_version(), serial=1 )
    #commands = list(filter(None, load_from_file('C:/Users/bertalan.pasztor/Documents/MLFF/trip_segment.txt')))
    commands = [
        "ALTER TABLE payment_transaction.payment_transaction DROP CONSTRAINT ck_paytran_psp_type;",
        "UPDATE payment_transaction.payment_transaction SET psp_type = 'FELLO' WHERE psp_type = 'FINNET';",
        "ALTER TABLE payment_transaction.payment_transaction ADD CONSTRAINT ck_paytran_psp_type CHECK (((psp_type)::text = ANY (ARRAY[('GOPAY'::character varying)::text, ('FELLO'::character varying)::text])));",
        "ALTER TABLE psp_clearing.psp_clearing DROP CONSTRAINT ck_pspcle_psp_type;",
        "UPDATE psp_clearing.psp_clearing SET psp_type = 'FELLO' WHERE psp_type = 'FINNET';",
        "ALTER TABLE psp_clearing.psp_clearing ADD CONSTRAINT ck_pspcle_psp_type CHECK (((psp_type)::text = ANY (ARRAY[('GOPAY'::character varying)::text, ('FELLO'::character varying)::text])));",
        "ALTER TABLE psp_clearing.psp_settlement_batch DROP CONSTRAINT ck_pspsettbat_psp_type;",
        "UPDATE psp_clearing.psp_settlement_batch SET psp_type = 'FELLO' WHERE psp_type = 'FINNET';",
        "ALTER TABLE psp_clearing.psp_settlement_batch ADD CONSTRAINT ck_pspsettbat_psp_type CHECK (((psp_type)::text = ANY (ARRAY[('GOPAY'::character varying)::text, ('FELLO'::character varying)::text])));",
        "ALTER TABLE psp_clearing.psp_settlement_package DROP CONSTRAINT ck_pspsettpac_psp_type;",
        "UPDATE psp_clearing.psp_settlement_package SET psp_type = 'FELLO' WHERE psp_type = 'FINNET';",
        "ALTER TABLE psp_clearing.psp_settlement_package ADD CONSTRAINT ck_pspsettpac_psp_type CHECK (((psp_type)::text = ANY (ARRAY[('GOPAY'::character varying)::text, ('FELLO'::character varying)::text])));",
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