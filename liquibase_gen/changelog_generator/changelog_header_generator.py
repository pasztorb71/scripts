from header_generator.Column import Column
from header_generator.Constraint import Constraint

import utils
from liquibase_gen.changelog_generator.main import get_template


class Changelog_header_generator():
    def __init__(self, author, jira, version='0.1.0'):
        self.author = author
        self.jira = jira
        self.comment = ''
        self.version = version
        self.changesetid = '01'

    def analyze_command(self):
        self.table_name = utils.get_tablename(self.command)
        self.schema_name = utils.get_schema(self.command)
        if ' column ' in command.lower():
            self.column_name = utils.get_columnname(self.command)
            self.commandtype = 'COLUMN'
        else:
            self.commandtype = ''


    def generate_header(self, command):
        return get_template(command)


    def gen_column_header(self, command):
        column = Column(command)
        column.set_comand(command)
        return column.get_header()

    def gen_constraint_header(self, command):
        cons = Constraint(command)
        return cons.get_header()


