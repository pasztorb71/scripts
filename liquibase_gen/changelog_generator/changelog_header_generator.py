import re

import utils
from liquibase_gen.changelog_generator.command_templates import *


class Changelog_header_generator():
    def __init__(self, author, jira, version='0.1.0'):
        self.author = author
        self.jira = jira
        self.comment = ''
        self.version = version
        self.changesetid = 0

    def analyze_command(self):
        self.table_name = utils.get_tablename_from_command(self.command)
        self.schema_name = utils.get_schema_from_command(self.command)
        if ' column ' in self.command.lower():
            self.column_name = utils.get_columnname_from_command(self.command)
            self.commandtype = 'COLUMN'
        else:
            self.commandtype = ''


    def generate_header(self, command):
        tmp = self.get_template(command)
        self.command = command
        return tmp\
            .replace('!!author!!', self.author)\
            .replace('!!table_upper!!',utils.get_tablename_from_command(self.command).upper())\
            .replace('!!version!!', self.version)\
            .replace('!!ticket!!', self.jira)\
            .replace('!!serial!!', self.get_next_serial())\
            .replace('!!colname!!', utils.get_columnname_from_command(self.command)) \
            .replace('!!schema!!', utils.get_schema_from_command(self.command))\
            .replace('!!table_lower!!', utils.get_tablename_from_command(self.command)) \
            .replace('!!consname!!', utils.get_consname_from_command(self.command))\
            .replace('!!indexname!!', utils.get_indexname_from_command(self.command)) \
            .replace('!!trigger!!', utils.get_triggername_from_command(self.command))

    def get_template(self, command):
        template = None
        if re.match('.*ADD COLUMN.*',command): template = tmp_add_column
        elif re.match('COMMENT ON COLUMN.*',command): template = tmp_comment
        elif re.match('.*ADD CONSTRAINT .* CHECK ',command): template = tmp_add_ck_constraint
        elif re.match('.*ADD CONSTRAINT .* FOREIGN KEY ',command): template = tmp_add_fk_constraint
        elif re.match('.*DROP CONSTRAINT.*',command): template = tmp_drop_constraint
        elif re.match('.*CREATE.*INDEX.*',command): template = tmp_cre_index
        elif re.match('.*DROP INDEX.*',command): template = tmp_drop_index
        elif re.match('UPDATE.*',command): template = tmp_update
        elif re.match('.*ALTER COLUMN.* SET DEFAULT ',command): template = tmp_set_default
        elif re.match('.*ALTER COLUMN.* DROP NOT NULL',command): template = tmp_drop_not_null
        elif re.match('.*ALTER COLUMN.* SET NOT NULL',command): template = tmp_set_not_null
        elif re.match('.*ALTER COLUMN.* TYPE ',command): template = tmp_column_type
        elif re.match('.*RENAME COLUMN.*',command): template = tmp_rename_column
        elif re.match('DROP TABLE.*',command): template = tmp_drop_table
        elif re.match('DROP TRIGGER.*',command): template = tmp_drop_trigger
        elif re.match('.* ADD .*',command): template = tmp_add_column
        elif re.match('.* DROP COLUMN .*',command): template = tmp_drop_column
        elif re.match('.*GRANT .*',command): template = tmp_grant
        elif re.match('.*ALTER INDEX .* RENAME .*',command): template = tmp_rename_index
        return template

    def get_next_serial(self):
        self.changesetid += 1
        return str(self.changesetid).rjust(2,'0')


