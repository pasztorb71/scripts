import pandas as pd

from Repository import Repository
from Ticket import Ticket
from liquibase_gen.gen_table.Confluence import Confluence
from liquibase_gen.gen_table.params import gen_table_params
import bs4 as bs

def modify_type(col):
    if col.startswith('enum'):
        return 'varchar(30)'
    return col.lower().replace('varchar2', 'varchar')\
        .replace('timestamp_with_timezone', 'timestamptz(6)')\
        .replace('decimal', 'numeric')\
        .replace('double', 'numeric')\
        .replace('smallint', 'int2')\
        .replace('blob', 'bytea').replace('number', 'numeric')


def get_table_from_confluence(table, url):
    conf = Confluence()
    html = conf.get_table_from_url(url)
    table_comment = conf.get_table_comment()
    tab = pd.read_html(html)
    #TODO enum keresés
    #parsed_html = bs.BeautifulSoup(html)
    #enums = get_enums(parsed_html)
    df = tab[0]
    a = list(df.columns)
    return table_comment, [list(df.columns)] + df.values.tolist()


def get_enums(parsed_html):
    for div in parsed_html.find_all(class_="confluenceTd"):
        a = div.text
    return None


def is_row_needed(name):
    return name.lower().startswith('x__') == False and not any(name.lower() == x for x in ['auditable fields', 'audit fields'])

def is_nan_or_none(name):
    return name == '' or pd.isnull(name)


def get_default_colval(defval, coltype):
    return "'" + defval + "'" if 'varchar' in coltype.lower() else defval


def check_type(colname, coltype):
    type = coltype.lower()
    if 'varchar' in type and not all(x in type for x in ['varchar', '(']):
        raise Exception("Varchar without length!, column: "+colname)


def table_columns(tab_name, table, tab_short_name):
    header = "CREATE TABLE " + tab_name + " (" + \
             "\n\tx__id varchar(30) NOT NULL," \
             "\n\tx__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP," \
             "\n\tx__insuser varchar(30) NOT NULL," \
             "\n\tx__moddate timestamptz(6) NULL," \
             "\n\tx__moduser varchar(30) NULL," \
             "\n\tx__version int8 NOT NULL DEFAULT 0,"
    print(header)
    colnames = table[0]
    constraints =[]
    for col in [row for row in table if is_row_needed(row[0])][1:]:
        if colnames[3].upper() == 'DEFAULT':
            default = ' DEFAULT ' + ("'"+str(col[3])+"'") if not is_nan_or_none(col[3]) else ''
            null = ' NULL' if any(col[2].lower() == x for x in ['nullable', 'yes']) else ' NOT NULL'
        else:
            default = ' DEFAULT ' + get_default_colval(str(col[2]), col[1]) if not is_nan_or_none(col[2]) else ''
            null = ' NULL' if is_nan_or_none(col[3]) or col[3].lower() == 'nullable' else ' NOT NULL'
        check_type(col[0], col[1])
        type = modify_type(col[1])
        print('\t' + col[0].lower() + ' ' + type + null + default + ',')
        if col[0].lower().endswith('_id'):
            constraints.append('CONSTRAINT fk_'+tab_short_name+'_'+col[0].lower()+' FOREIGN KEY ('+col[0].lower()+') REFERENCES '+col[0].lower().split('_id')[0]+'(x__id) DEFERRABLE')
        if 'enum' in col[1].lower():
            constraints.append('CONSTRAINT ck_'+tab_short_name+'_'+col[0].lower()+f" CHECK ((({col[0].lower()})::text = ANY (ARRAY[('{col[1].split('enum')[1]}'::character varying)::text]))),")
        if 'check(' in col[1].lower():
            constraints.append('CONSTRAINT ck_' + tab_short_name + '_' + col[0].lower() + f" CHECK ((({col[0].lower()})::text = ANY (ARRAY[(''::character varying)::text]))),")
    print('\t' + 'CONSTRAINT pk_' + tab_name + ' PRIMARY KEY (x__id)', end='')
    if constraints:
        print(',\n\t' + ',\n\t'.join(constraints))
    print(');')

def table_comments(tab_comment, tab_name, table):
    print("COMMENT ON TABLE " + tab_name + " IS '" + tab_comment + "';\n")
    header = """-- Column comments

COMMENT ON COLUMN !table!.x__id IS 'Unique identifier';
COMMENT ON COLUMN !table!.x__insdate IS 'Date of creation';
COMMENT ON COLUMN !table!.x__insuser IS 'Identifier of creator user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN !table!.x__moddate IS 'Date of last modification';
COMMENT ON COLUMN !table!.x__moduser IS 'Identifier of modifier user, without FK (nonFK -> SECURITY_USER.X__ID)';
COMMENT ON COLUMN !table!.x__version IS 'Versioning of changes';""".replace('!table!', tab_name)
    print(header)
    for col in [row for row in table if is_row_needed(row[0])][1:]:
        modified_comment = col[4].replace("'", "''")
        print('COMMENT ON COLUMN ' + tab_name + "." + col[0].lower() + " IS '" + modified_comment + "';")


def table_grants(tab_name, ticket_name, version):
    t = tab_name.split('.')
    sema = t[0]
    table = tab_name
    print("""-- GRANT ==
ALTER TABLE !table! OWNER TO ${schema_name}_tbl_own;

GRANT SELECT ON TABLE !table! TO ${schema_name}_sel;
GRANT INSERT, UPDATE ON TABLE !table! TO ${schema_name}_mod;
GRANT DELETE, TRUNCATE ON TABLE !table! TO ${schema_name}_del;

""".replace('!table!', table).replace('!TABLE!', table.upper()).replace('!sema!', sema).replace('!!version!!', version).replace('!!ticket!!',ticket_name))


def table_header(sema, tab_name, ticket_name, version):
    t = tab_name.split('.')
    table = tab_name
    print("""--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:!TABLE!-DDL-!!ticket!!-01 runOnChange:true
--comment A !table! tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = '!sema!' AND tablename = '!table!';
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};
""".replace('!table!', table).replace('!TABLE!', table.upper()).replace('!sema!', sema).replace('!!version!!', version).replace('!!ticket!!',ticket_name))


def table_history(tab_name, ticket_name, version):
    t = tab_name.split('.')
    table = tab_name
    print("""--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:!TABLE!$HIST-DDL-!!ticket!!-01 runOnChange:true
--comment A !table!$hist history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = '!sema!' AND tablename = '!table!$hist';
---------------------------------------------------------------------------------------------------
SET search_path = ${schema_name};

call ${schema_name}.HIST_TABLE_GENERATOR('${schema_name}', '!table!');

-- GRANT$HIST ==
GRANT SELECT ON TABLE !table!$hist TO ${schema_name}_sel;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
call ${schema_name}.HIST_TRIGGER_GENERATOR('${schema_name}', '!table!');

""".replace('!table!', table).replace('!TABLE!', table.upper()).replace('!!version!!', version).replace('!!ticket!!',ticket_name))


def table_indexes(tab_name, table, tab_short_name):
    for col in [row for row in table if is_row_needed(row[0])][1:]:
        if col[0].lower().endswith('_id'):
            print('CREATE INDEX ix_'+tab_short_name+'_'+col[0].lower()+' ON '+tab_name+' USING btree ('+col[0].lower()+');')


def print_table_script(tab_comment, schema_name, tab_name, table, history, ticket_name, version):
    print('--liquibase formatted sql\n')
    table_header(schema_name, tab_name, ticket_name, version)
    table_columns(tab_name, table, tab_short_name)
    print()
    table_indexes(tab_name, table, tab_short_name)
    print()
    table_comments(tab_comment, tab_name, table)
    print()
    table_grants(tab_name, ticket_name, version)
    if history == 'y':
        table_history(tab_name, ticket_name, version)


def create_tablefile(repo:Repository, tab_name):
    if not repo.is_table_file_exists(tab_name):
        print(f"DDL file: {repo.get_tables_dir()}/{tab_name}/{tab_name}-DDL-000.sql")
        if input("Create DDL file? [y/n]") == "y":
            repo.create_tablefile(tab_name)
            #TODO javítani
            #repo.schema_version_xml(tab_name)
        else:
            print('DDL file not created!')


if __name__ == '__main__':
    #TODO könyvtár és fájl létrehozása, esetleg beírás a create_table.sql-be is
    params = gen_table_params
    ticket = Ticket(params['ticket'])
    repo = Repository(params['repo'])
    base = repo.get_base_path()
    tab_name = params['tablename'].split('.')[1].lower()
    schema_name = params['tablename'].split('.')[0].lower()
    tab_short_name = params['table_shortname']
    history = params['history']
    url = params['url']
    db = repo.get_db_name()
    db_path = db.replace('-', '_')
    create_tablefile(repo, tab_name)
    #TODO beírni a create-tables.xml-be
    tab_comment, table = get_table_from_confluence(tab_name, url)
    print_table_script(tab_comment, schema_name, tab_name, table, history, ticket_name=ticket.name, version=ticket.get_version())

