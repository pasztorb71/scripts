import glob
import os
import re
from pathlib import Path

from sqlalchemy import MetaData

from liquibase_gen.changelog_generator.changelog_header_generator import Changelog_header_generator
from liquibase_gen.changelog_generator.command_templates import *


def create_table():
    metadata_obj = MetaData()
    user_preference = Table('customer', metadata_obj,
        Column('pref_id', Integer, primary_key=True),
        Column('user_id', Integer, ForeignKey("user.user_id"), nullable=False),
        Column('pref_name', String(40), nullable=False),
        Column('pref_value', String(100),
        Column('date_done', DateTime(timezone=True), server_default=func.now(), nullable=False, comment='Date of creation'))
    )


def get_command_type(stmt):
    pass


def is_command_need(l):
    return l.startswith('--') == False and l and 'commit' not in l.lower() and l.startswith('call') == False


def get_template(command):
    template = None
    for cmd in commands:
        if re.match('.*ADD COLUMN.*',cmd): template = tmp_add_column
        elif re.match('COMMENT ON COLUMN.*',cmd): template = tmp_comment
        elif re.match('.*ADD CONSTRAINT .* CHECK ',cmd): template = tmp_add_ck_constraint
        elif re.match('.*ADD CONSTRAINT .* FOREIGN KEY ',cmd): template = tmp_add_fk_constraint
        elif re.match('.*DROP CONSTRAINT.*',cmd): template = tmp_drop_constraint
        elif re.match('.*CREATE INDEX.*',cmd): template = tmp_cre_index
        elif re.match('.*DROP INDEX.*',cmd): template = tmp_drop_index
        elif re.match('UPDATE.*',cmd): template = tmp_update
        elif re.match('.*ALTER COLUMN.* SET DEFAULT ',cmd): template = tmp_set_default
        elif re.match('.*ALTER COLUMN.* DROP NOT NULL',cmd): template = tmp_drop_not_null
        elif re.match('.*ALTER COLUMN.* SET NOT NULL',cmd): template = tmp_set_not_null
        elif re.match('.*ALTER COLUMN.* TYPE ',cmd): template = tmp_column_type
        elif re.match('.*RENAME COLUMN.*',cmd): template = tmp_rename_column
        elif re.match('DROP TABLE.*',cmd): template = tmp_drop_table
        elif re.match('DROP TRIGGER.*',cmd): template = tmp_drop_trigger
        elif re.match('.* ADD .*',cmd): template = tmp_add_column
        elif re.match('.* DROP COLUMN .*',cmd): template = tmp_drop_column
        elif re.match('.*GRANT .*',cmd): template = tmp_grant
        elif re.match('.*ALTER INDEX .* RENAME .*',cmd): template = tmp_rename_index
    return template


if __name__ == '__main__':
    g = Changelog_header_generator(author='bertalan.pasztor',jira='a', version='0.3.0' )
    commands = ['ALTER TABLE exemption.exemption_vehicle ALTER COLUMN plate_number TYPE varchar(32) USING plate_number::varchar;']
    for stmt in commands:
        header = g.generate_header(commands)
