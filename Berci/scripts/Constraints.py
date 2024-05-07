import re


class Constraint():
    def __init__(self, type, name, schema, tabname, colname, definition):
        self.type = type
        self.name = name
        self.schema = schema
        self.tabname = tabname
        self.colname = colname
        self.definition = definition

    def __str__(self):
        return f'{self.schema}.{self.tabname}({self.colname})'

    @property
    def enums_in_constraint(self):
        pattern = r"ARRAY\[(.*?)\]"
        try:
            array_text = re.search(pattern, self.definition).group(1)
            possible_values = re.findall(r"'(.*?)'", array_text)
            return possible_values
        except AttributeError:
            return None