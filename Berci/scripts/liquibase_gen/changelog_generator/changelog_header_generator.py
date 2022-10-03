import re

import utils
from liquibase_gen.changelog_generator.command_templates import *


class Changelog_header_generator():
    def __init__(self, author, jira, version='0.1.0', serial=0):
        self.author = author
        self.jira = jira
        self.comment = ''
        self.version = version
        self.serial = serial
        self.original_serial = serial
        self.table_name = ''
        self.prev_table = ''
        self.prev_column = ''

    def generate_header(self, repo, command, hist=False):
        tmp = self.get_template(command)
        table_name = utils.get_tablename_from_command(repo, command)
        if self.prev_table == '':
            self.prev_table = table_name
        column_name = utils.get_columnname_from_command(command)
        if table_name == self.prev_table and column_name == self.prev_column and command.startswith('COMMENT ON COLUMN'):
            return '',''

        try:
            tmp = tmp\
                .replace('!!author!!', self.author)\
                .replace('!!table_upper!!',table_name.upper())\
                .replace('!!version!!', self.version)\
                .replace('!!ticket!!', self.jira)\
                .replace('!!serial!!', self.get_next_serial(table_name.lower()))\
                .replace('!!colname!!', utils.get_columnname_from_command(command)) \
                .replace('!!schema!!', utils.get_schema_from_command(command))\
                .replace('!!table_lower!!', table_name.lower()) \
                .replace('!!consname!!', utils.get_consname_from_command(command))\
                .replace('!!indexname!!', utils.get_indexname_from_command(command)) \
                .replace('!!trigger!!', utils.get_triggername_from_command(command))
        except AttributeError as e:
            print(f'Hibás parancs :{command}')
            raise e

        if self.is_newtable(table_name) and '$hist' in table_name:
            tmp = self.get_hist_header() + tmp
        self.prev_table = table_name
        self.prev_column = column_name

        return tmp, table_name

    def get_template(self, command):
        template = None
        if re.match('.*ADD COLUMN.*',command): template = tmp_add_column
        elif re.match('COMMENT ON COLUMN.*',command): template = tmp_comment_column
        elif re.match('COMMENT ON TABLE.*',command): template = tmp_comment_table
        elif re.match('.*ADD CONSTRAINT .* CHECK ',command): template = tmp_add_ck_constraint
        elif re.match('.*RENAME CONSTRAINT .*',command): template = tmp_rename_constraint
        elif re.match('.*ADD CONSTRAINT .* FOREIGN KEY ',command): template = tmp_add_fk_constraint
        elif re.match('.*DROP CONSTRAINT.*',command): template = tmp_drop_constraint
        elif re.match('.*CREATE.*INDEX.*',command): template = tmp_cre_index
        elif re.match('.*DROP INDEX.*',command): template = tmp_drop_index
        elif re.match('UPDATE.*',command): template = tmp_update
        elif re.match('DELETE.*',command): template = tmp_delete
        elif re.match('TRUNCATE TABLE.*',command): template = tmp_delete
        elif re.match('.*ALTER COLUMN.* SET DEFAULT ',command): template = tmp_set_default
        elif re.match('.*ALTER COLUMN.* DROP NOT NULL',command): template = tmp_drop_not_null
        elif re.match('.*ALTER COLUMN.* SET NOT NULL',command): template = tmp_set_not_null
        elif re.match('.*ALTER TABLE.* DROP DEFAULT',command): template = tmp_drop_default
        elif re.match('.*ALTER COLUMN.* TYPE ',command): template = tmp_column_type
        elif re.match('.*RENAME COLUMN.*',command): template = tmp_rename_column
        elif re.match('DROP TABLE.*',command): template = tmp_drop_table
        elif re.match('DROP TRIGGER.*',command): template = tmp_drop_trigger
        elif re.match('.* ADD .*',command): template = tmp_add_column
        elif re.match('.* DROP COLUMN .*',command): template = tmp_drop_column
        elif re.match('.*GRANT .*',command): template = tmp_grant
        elif re.match('.*ALTER INDEX .* RENAME .*',command): template = tmp_rename_index
        elif re.match('ALTER SCHEMA .* RENAME TO .*',command): template = tmp_rename_schema
        elif re.match('ALTER TABLE .* RENAME TO .*',command): template = tmp_rename_table
        elif re.match('INSERT INTO .* ',command): template = tmp_insert_into_table
        elif not command : template = tmp_trigger_section
        return template

    def get_hist_header(self):
        return """
--===============================================================================================--
-- HISTORY ==
"""

    def is_newtable(self, table_name):
        return table_name != self.prev_table

    def get_next_serial(self, table_name):
        if not self.is_newtable(table_name):
            self.serial += 1
            out = str(self.serial).rjust(2, '0')
        else:
            self.serial = self.original_serial + 1
            out = str(self.serial).rjust(2,'0')
            #self.prev_table = table_name
        return out

    def generate_trigger_section(self):
        tmp = tmp_trigger_section
        tmp = tmp \
            .replace('!!author!!', self.author) \
            .replace('!!table_upper!!', self.prev_table.upper()) \
            .replace('!!version!!', self.version) \
            .replace('!!ticket!!', self.jira) \
            .replace('!!serial!!', '01') \
            .replace('!!table_lower!!', self.prev_table.lower()) \
            .replace('!!table_nohist!!', self.prev_table.lower().replace('$hist', ''))
        return '\n\n' + tmp

    @staticmethod
    def generate_commandblock(header, stmt, tablename):
        arr = header.split('\n')
        if arr[2] == '-- HISTORY ==':
            expected = re.match(".*expectedResult:([0-9]) SELECT", arr[8]).group(1)
            pre = re.match(".*count\\(\\*\\) (.*)", arr[8]).group(1)
        else:
            expected = re.match(".*expectedResult:([0-9]) SELECT", arr[5]).group(1)
            pre = re.match(".*count\\(\\*\\) (.*)", arr[5]).group(1)
        pre = utils.format_sql(pre)
        cmd = """  cnt := -1;
  SELECT count(*) INTO cnt 
    !!precond!!;
    
  IF cnt = !!expected!! THEN --<< expectedResult --
    !!command!!;
  END IF;
"""
        return cmd.replace('!!precond!!', pre).replace('!!expected!!', expected).replace('!!command!!', stmt)


    def gen_new_header_from_old(self, header, tablename):
        arr = header.split('\n')
        arr[1] = re.sub('-[0-9].[0-9]{2}.[0.9]-', '-', arr[1]) + ' endDelimiter:/'
        s = arr[0:3] + [arr[0]]
        return '\n'.join(s) + """\nSET search_path = ${schema_name};
        
DO $$
DECLARE
  cnt int;
  v_schema_name text := '${schema_name}';  
BEGIN
"""


