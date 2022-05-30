import re


def get_tablename(command):
    m = re.match("ALTER TABLE (\w+[.])?([a-zA-z0-9_]+)", command)
    return m.group(2)


def get_columnname(command):
    m = re.match(".* COLUMN ([a-zA-z0-9._]+) ", command)
    return m.group(1)


def get_schema(command):
    m = re.match("ALTER TABLE ([a-zA-z0-9_]+)", command)
    return m.group(1)