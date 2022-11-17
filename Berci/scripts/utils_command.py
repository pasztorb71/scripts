import re


def get_columnname_from_command(command):
    command = command.replace('IF EXISTS ','').replace('"','')
    m = None
    if 'DROP COLUMN ' in command:
        m = re.match(".* DROP COLUMN (\w+)", command)
    elif ' COLUMN ' in command:
        m = re.match(".* COLUMN ([a-zA-z0-9._\"$]+) ", command)
    elif ' ADD ' in command and 'CONSTRAINT' not in command:
        m = re.match(".* ADD ([a-zA-z0-9._\"]+) ", command)
    elif ' ADD CONSTRAINT' in command:
        m = re.match(".* CHECK \(\(\((\w+)", command)
    elif 'UPDATE ' in command:
        m = re.match("UPDATE .* SET (\w+)", command)
    return m.group(1).split('.')[-1].replace('"','') if m else ''


def get_schema_from_command(command):
    command = command.replace('IF EXISTS ','').replace('"','')
    patterns = ["ALTER SCHEMA ([a-zA-z0-9_\"]+) ",
                "ALTER TABLE ([a-zA-z0-9_\"]+)",
                "COMMENT ON COLUMN ([a-zA-z0-9_\"]+)",
                ".* INDEX .* (?:ON )([a-zA-z0-9_\"]+)",
                "UPDATE ([a-zA-z0-9_\"]+)",
                "DELETE FROM ([a-zA-z0-9_\"]+)",
                "DROP INDEX (.*)\.",
                "GRANT .* ON TABLE \${schema_name_(\w+)",
                ".* TABLE ([a-zA-z0-9_\"]+)",
                ".*TRIGGER .*ON \${schema_name_(\w+)",
                "ALTER INDEX (\w+)"]
    outs = [re.match(pattern, command) for pattern in patterns]
    try:
        m = next(item for item in outs if item is not None)
    except:
        m = None
    return m.group(1).replace('"','') if m else ''


def get_consname_from_command(command):
    command = command.replace('IF EXISTS ', '').replace('"', '')
    m = re.match(".*CONSTRAINT (\w+)[;]?", command)
    return m.group(1) if m else ''


def get_indexname_from_command(command):
    command = command.replace('IF EXISTS ', '').replace('"', '')
    patterns = ["DROP INDEX .*\.(\w+)",
                "ALTER INDEX .*\.(\w+) RENAME TO \w+",
                ".* INDEX (\w+)[;]?",]
    outs = [re.match(pattern, command) for pattern in patterns]
    try:
        m = next(item for item in outs if item is not None)
    except:
        m = None
    return m.group(1)  if m else ''


def get_triggername_from_command(command):
    m = re.match(".*TRIGGER (?:IF EXISTS) ([a-zA-z0-9_$\"]+)[;]?", command)
    return m.group(1)  if m else ''


def get_tablename_from_command(repo, command):
    command = command.replace('IF EXISTS ','').replace('"','')
    if command.startswith('DROP INDEX '):
        return repo.get_tablename_from_indexname(command.replace('DROP INDEX ', '').replace(';', ''))
    patterns = ["ALTER TABLE (\w+[.])?([a-zA-z0-9_$\"]+)",
                "COMMENT ON COLUMN (\w+[.])?([a-zA-z0-9_$\"]+)",
                "CREATE.*INDEX .* ON (\w+)[.]?([a-zA-z0-9_$\"]+)",
                "UPDATE (\w+[.])?([a-zA-z0-9_\"]+)",
                "DELETE FROM (\w+[.])?([a-zA-z0-9_\"]+)",
                "GRANT .* ON TABLE (\${.*}).(.*) TO ",
                ".* TABLE (\w+[.])?([a-zA-z0-9_$\"]+)",
                "INSERT INTO (\w+[.])?([a-zA-z0-9_\"]+)",
                ]
    outs = [re.match(pattern, command) for pattern in patterns]
    try:
        m = next(item for item in outs if item is not None)
    except:
        m = None
    if outs[2]:                     # CREATE.*INDEX
        return m.group(2)
    return m.group(2).replace('"','') if m else ''