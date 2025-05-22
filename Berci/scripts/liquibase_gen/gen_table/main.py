import pandas as pd

from classes.Project import choose_project
from classes.Repository import Repository
from classes.Ticket import Ticket
from liquibase_gen.gen_table.Confluence import Confluence
from liquibase_gen.gen_table.params import event, event_input, event_validation_result, event_status_process, event_catalog, event_catalog_item


def modify_type(col):
    if col.startswith('enum'):
        return 'varchar(30)'
    return col.lower().replace('varchar2', 'varchar')\
        .replace('timestamp_with_timezone', 'timestamptz(6)')\
        .replace('timestamptz(nan)', 'timestamptz(6)')\
        .replace('decimal', 'numeric')\
        .replace('double', 'numeric')\
        .replace('smallint', 'int2')\
        .replace('blob', 'bytea')\
        .replace('number', 'numeric')\
        .replace('int(nan)', 'int')


def get_table_from_confluence(table, url, start_string=None):
    conf = Confluence()
    html = conf.get_table_from_url(url, start_string)
    table_comment = conf.get_table_comment()
    tab = pd.read_html(html)
    df = tab[0]
    df = df.astype(str)
    a = list(df.columns)
    b = df.values.tolist()
    return table_comment, [list(df.columns)] + df.values.tolist()


def is_row_needed(name):
    return name.lower().startswith('x__') == False and not any(name.lower() == x for x in ['auditable fields', 'audit fields'])

def is_nan_or_none(name):
    return name == '' or pd.isnull(name) or name in ('-', '', 'nan')


def get_default_colval(defval, coltype):
    return "'" + defval + "'" if 'varchar' in coltype.lower() else defval


def check_type(colname, coltype, database_type):
    type = coltype.lower()
    if database_type != 'trino':
        if 'varchar' in type and not all(x in type for x in ['varchar', '(']):
            raise Exception("Varchar without length!, column: "+colname)


def gen_table_columns(tab_name, table, tab_short_name, database_type):
    if database_type != 'trino':
        nullable_col = 3
        header = "CREATE TABLE " + tab_name + " (" + \
                 "\n\tx__id varchar(30) NOT NULL," \
                 "\n\tx__insdate timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP," \
                 "\n\tx__insuser varchar(30) NOT NULL DEFAULT '0'," \
                 "\n\tx__moddate timestamp NULL," \
                 "\n\tx__moduser varchar(30) NULL," + \
                 "\n\tx__version int8 NOT NULL DEFAULT 0,"
    else:
        nullable_col = 2
        header = "CREATE TABLE ${schema_name}." + tab_name + " (" + \
                 "\n\tx__id varchar NOT NULL," \
                 "\n\tx__insdate timestamp NOT NULL," \
                 "\n\tx__insuser varchar NOT NULL," \
                 "\n\tx__moddate timestamp," \
                 "\n\tx__moduser varchar," + \
                 "\n\tx__version smallint NOT NULL,"
    script = header
    colnames = table[0]
    constraints =[]
    for col in [row for row in table if is_row_needed(row[0])][1:]:
        if 'DEFAULT' in colnames[3].upper():
            a = is_nan_or_none(col[3])
            default = ' DEFAULT ' + ("'"+str(col[3])+"'") if not is_nan_or_none(col[3]) else ''
            null = ' NULL' if any(col[2].lower() == x for x in ['nullable', 'yes']) else ' NOT NULL'
        elif colnames[nullable_col].upper() in ['NOT NULL', 'NULLABLE']:
            default = ''
            pos = 2 if database_type == 'trino' else 3
            is_null = is_nullable(col, pos)
            if database_type == 'trino':
                null = '' if is_null else ' NOT NULL'
            else:
                null = ' NULL' if is_null else ' NOT NULL'
        else:
            if database_type == 'trino':
                default = ''
            else:
                default = ' DEFAULT ' + get_default_colval(str(col[2]), col[1]) if not is_nan_or_none(col[2]) else ''
            null = ' NULL' if is_nullable(col) else ' NOT NULL'
        if colnames[3] == 'NOT NULL':
            col[1] = f"{col[1]}({col[2].split('.')[0]})"
        check_type(col[0], col[1], database_type)
        type = modify_type(col[1])
        script += '\n\t' + col[0].lower() + ' ' + type + null + default + ','
        if database_type == 'trino':
            continue
        if col[0].lower().endswith('_id'):
            constraints.append('CONSTRAINT fk_'+tab_short_name+'_'+col[0].lower()+' FOREIGN KEY ('+col[0].lower()+') REFERENCES '+col[0].lower().split('_id')[0]+'(x__id)')
        if 'enum' in col[1].lower():
            constraints.append('CONSTRAINT ck_'+tab_short_name+'_'+col[0].lower()+f" CHECK ((({col[0].lower()})::text = ANY (ARRAY[('{col[1].lower().split('enum')[1]}'::character varying)::text]))),")
        if any([x  in col[1].lower() for x in ('check(','check (')]):
            constraints.append('CONSTRAINT ck_' + tab_short_name + '_' + col[0].lower() + f" CHECK ((({col[0].lower()})::text = ANY (ARRAY[(''::character varying)::text]))),")
    if database_type != 'trino':
        script += '\n\t' + 'CONSTRAINT pk_' + tab_name + ' PRIMARY KEY (x__id)'
    else:
        script = script[:-1]
    if constraints:
         script += ',\n\t' + ',\n\t'.join(constraints)
    script += '\n);'
    return script


def is_nullable(row, col=3):
    return is_nan_or_none(row[col]) or row[col].lower() in ('nullable', 'false', 'nan')


def gen_table_comments(tab_comment, tab_name, table, language, database_type='postgres'):
    comment_col = 3 if database_type == 'trino' else 5
    script = "COMMENT ON TABLE " + tab_name + " IS '" + tab_comment + "';\n\n"
    header = "-- Column comments\n"
    if language == 'eng':
        header += f"""COMMENT ON COLUMN {tab_name}.x__id IS 'Unique identifier';
COMMENT ON COLUMN {tab_name}.x__insdate IS 'Date of creation';
COMMENT ON COLUMN {tab_name}.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN {tab_name}.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN {tab_name}.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN {tab_name}.x__version IS 'Versioning of changes';"""
    if language == 'hu':
        header += f"""COMMENT ON COLUMN {tab_name}.x__id IS 'Elsődleges kulcs';
COMMENT ON COLUMN {tab_name}.x__insdate IS 'A beszúrás időpontja';
COMMENT ON COLUMN {tab_name}.x__insuser IS 'A beszúrást végző felhasználó azonosítója (X__ID)';
COMMENT ON COLUMN {tab_name}.x__moddate IS 'Az utolsó módosítás időpontja';
COMMENT ON COLUMN {tab_name}.x__moduser IS 'A módosítást végző felhasználó azonosítója (X__ID)';
COMMENT ON COLUMN {tab_name}.x__version IS 'Változás verziózása';"""
    script += header
    for col in [row for row in table if is_row_needed(row[0])][1:]:
        modified_comment = col[comment_col].replace("'", "''")
        script += '\nCOMMENT ON COLUMN ' + tab_name + "." + col[0].lower() + " IS '" + modified_comment + "';"
    return script


def gen_table_grants(tab_name, ticket_name, version):
    t = tab_name.split('.')
    table = tab_name
    return """-- GRANT 
CALL public.add_privileges_to_table('${schema_name}', '!table!');

""".replace('!table!', tab_name)


def gen_table_header(sema, tab_name, ticket_name, version, sequence, database_type):
    search_path = 'SET search_path = ${schema_name};\n' if database_type != 'trino' else ''
    return ("""--changeset bertalan.pasztor:${schema_name_new}-""" + f"""{sequence}
--comment {ticket_name} {tab_name.upper()} tábla létrehozása\n""" + search_path).replace('!schema!', '${schema_name}')


def gen_table_history(sema, tab_name, ticket_name, version):
    t = tab_name.split('.')
    return """-- HISTORY 
CALL public.hist_table_generator('${schema_name}', '!table!');
CALL public.hist_trigger_generator('${schema_name}', '!table!');
CALL public.add_privileges_to_table('${service_name}', '!table!$hist');

""".replace('!table!', tab_name)

def gen_table_indexes(tab_name, table, tab_short_name):
    for col in [row for row in table if is_row_needed(row[0])][1:]:
        if col[0].lower().endswith('_id') or col[0].lower().endswith('_refid'):
            return 'CREATE INDEX ix_'+tab_short_name+'_'+col[0].lower()+' ON '+tab_name+' USING btree ('+col[0].lower()+');'
    return ''

def gen_table_script(tab_comment, schema_name, tab_name, table, history, ticket_name, version, language, sequence, database_type='postgres'):
    script = '--liquibase formatted sql\n'
    script += gen_table_header(schema_name, tab_name, ticket_name, version, sequence, database_type)
    script += '\n'
    script += gen_table_columns(tab_name, table, tab_short_name, database_type)
    if database_type != 'trino':
        script += '\n\n'
        script += gen_table_indexes(tab_name, table, tab_short_name)
        script += '\n\n'
    script += gen_table_comments(tab_comment, tab_name, table, language, database_type)
    script += '\n\n'
    if database_type != 'trino':
        script += gen_table_grants(tab_name, ticket_name, version)
        if history == 'y':
            script += gen_table_history(schema_name, tab_name, ticket_name, version)
        script += 'COMMIT;\n'
    return script

def create_tablefile(repo:Repository, tab_name, sequence, tabscript):
    new_type_repo = repo.is_new_type_sql_numbering()
    #TODO új típust megcsinálni
    if not repo.is_table_file_exists(tab_name):
        filename = f"{repo.get_tables_dir()}/{tab_name}/{sequence}-{tab_name}-create.sql"
        print(f'tab_name: {tab_name}')
        print(f'filename: {filename}')
        if input("Create DDL file? [y/n]") == "y":
            repo.create_tablefile(tab_name, tabscript, filename)
            #TODO javítani
            #repo.schema_version_xml(tab_name)
        else:
            print(tabscript)


if __name__ == '__main__':
    reponame = 'emap-org'  # AKP
    params_list = [event, event_input, event_validation_result, event_status_process, event_catalog, event_catalog_item]
    for params in params_list:
        ticket = Ticket(params['ticket'])
        project = choose_project(reponame)
        repo = Repository(reponame, proj=project)
        base = repo.get_base_path()
        tab_name = params['tablename'].split('.')[1].lower()
        schema_name = params['tablename'].split('.')[0].lower()
        repo._schema = schema_name
        tab_short_name = params['table_shortname']
        history = params['history']
        url = params['url']
        db = repo.get_db_name()
        db_path = db.replace('-', '_')
        #TODO beírni a create-tables.xml-be
        tab_comment, table = get_table_from_confluence(tab_name, url, params.get('start_string'))
        database_type = params['database_type'] if 'database_type' in params else 'postgres'
        tabscript = gen_table_script(tab_comment, schema_name, tab_name, table, history,
                                     ticket.name, ticket.get_version(), params['language'], params['sequence'], database_type)
        create_tablefile(repo, tab_name, params['sequence'], tabscript)

