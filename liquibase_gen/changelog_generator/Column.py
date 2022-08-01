from header_generator import header_templates


class Column:
    def __init__(self, command):
        pass

    def get_header(self):
        precondition_column = header_templates.precondition_column
        table_ddl_template = header_templates.column_template
        precond = precondition_column \
            .replace('###schema###', self.schema_name) \
            .replace('###table###', self.table_name) \
            .replace('###column###', self.column_name)
        header = table_ddl_template \
            .replace('###author###', self.author) \
            .replace('###table###', self.table_name.upper()) \
            .replace('###version###', self.version) \
            .replace('###jira###', self.jira) \
            .replace('###changesetid###', self.changesetid) \
            .replace('###comment###', self.comment) \
            .replace('###precondition###', precond)
        return header