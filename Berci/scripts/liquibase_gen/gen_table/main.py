import math

import pandas as pd

from Repository import Repository
from liquibase_gen.gen_table.Confluence import Confluence
from liquibase_gen.gen_table.params import gen_table_params


def modify_type(col):
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
    df = tab[0]
    a = list(df.columns)
    return table_comment, [list(df.columns)] + df.values.tolist()

def is_col_needed(name):
    return name.lower().startswith('x__') == False and name.lower() != 'auditable fields'

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
    fk =[]
    for col in [row for row in table if is_col_needed(row[0])][1:]:
        if colnames[3].upper() == 'DEFAULT':
            default = ' DEFAULT ' + ("'"+str(col[3])+"'") if not is_nan_or_none(col[3]) else ''
            null = ' NULL' if col[2].lower() == 'nullable' else ' NOT NULL'
        else:
            default = ' DEFAULT ' + get_default_colval(str(col[2]), col[1]) if not is_nan_or_none(col[2]) else ''
            null = ' NULL' if is_nan_or_none(col[3]) or col[3].lower() == 'nullable' else ' NOT NULL'
        check_type(col[0], col[1])
        type = modify_type(col[1])
        print('\t' + col[0].lower() + ' ' + type + null + default + ',')
        if col[0].lower().endswith('_id'):
            fk.append('CONSTRAINT fk_'+tab_short_name+'_'+col[0].lower()+' FOREIGN KEY ('+col[0].lower()+') REFERENCES '+tab_name.split('.')[0]+'.'+col[0].lower().split('_')[0]+'(x__id) DEFERRABLE')
    print('\t' + 'CONSTRAINT pk_' + tab_name.split('.')[1] + ' PRIMARY KEY (x__id)', end='')
    if fk:
        print(',\n\t' + ',\n\t'.join(fk))
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
    for col in [row for row in table if is_col_needed(row[0])][1:]:
        modified_comment = col[4].replace("'", "''")
        print('COMMENT ON COLUMN ' + tab_name + "." + col[0].lower() + " IS '" + modified_comment + "';")


def table_grants(tab_name):
    t = tab_name.split('.')
    sema = t[0]
    table = t[1]
    print("""--===============================================================================================--
-- GRANT ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:!TABLE!_GRANT runOnChange:true
--comment A !table! táblára jogosultságok kiosztása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_tables WHERE schemaname = '!sema!' AND tablename = '!table!';
---------------------------------------------------------------------------------------------------

ALTER TABLE !sema!.!table! OWNER TO ${schema_name}_tbl_own;

GRANT SELECT ON TABLE !sema!.!table! TO ${schema_name}_sel;
GRANT INSERT, UPDATE ON TABLE !sema!.!table! TO ${schema_name}_mod;
GRANT DELETE, TRUNCATE ON TABLE !sema!.!table! TO ${schema_name}_del;

""".replace('!table!', table).replace('!TABLE!', table.upper()).replace('!sema!', sema))


def table_header(tab_name):
    t = tab_name.split('.')
    sema = t[0]
    table = t[1]
    print("""--===============================================================================================--
-- TABLE ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:!TABLE! runOnChange:true
--comment A !table! tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = '!sema!' AND tablename = '!table!';
---------------------------------------------------------------------------------------------------
""".replace('!table!', table).replace('!TABLE!', table.upper()).replace('!sema!', sema))


def table_history(tab_name):
    t = tab_name.split('.')
    sema = t[0]
    table = t[1]
    print("""--===============================================================================================--
-- HISTORY ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:!TABLE!$HIST runOnChange:true
--comment A !table!$hist history tábla létrehozása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:0 SELECT count(*) FROM pg_tables WHERE schemaname = '!sema!' AND tablename = '!table!$hist';
---------------------------------------------------------------------------------------------------

call ${schema_name}.HIST_TABLE_GENERATOR('${schema_name}', '!table!');


--===============================================================================================--
-- GRANT$HIST ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:!TABLE!$HIST_GRANT runOnChange:true
--comment A !table!$hist táblára Select jog kiosztása..
--
--preconditions onFail:MARK_RAN onError:HALT
--precondition-sql-check expectedResult:1 SELECT count(*) FROM pg_tables WHERE schemaname = '!sema!' AND tablename = '!table!$hist';
---------------------------------------------------------------------------------------------------

GRANT SELECT ON TABLE !sema!.!table!$hist TO ${schema_name}_sel;


--===============================================================================================--
-- TRIGGER ==
---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:TR_!TABLE!$HIST runOnChange:true
--comment A tr_!table!$hist trigger létrehozása..
---------------------------------------------------------------------------------------------------

call ${schema_name}.HIST_TRIGGER_GENERATOR('${schema_name}', '!table!');

""".replace('!table!', table).replace('!TABLE!', table.upper()).replace('!sema!', sema))


def table_indexes(tab_name, table, tab_short_name):
    for col in [row for row in table if is_col_needed(row[0])][1:]:
        if col[0].lower().endswith('_id'):
            print('CREATE INDEX ix_'+tab_short_name+'_'+col[0].lower()+' ON '+tab_name+' USING btree ('+col[0].lower()+');')


def print_table_script(tab_comment, tab_name, table, history):
    print('--liquibase formatted sql\n')
    table_header(tab_name)
    table_columns(tab_name, table, tab_short_name)
    print()
    table_indexes(tab_name, table, tab_short_name)
    print()
    table_comments(tab_comment, tab_name, table)
    print()
    table_grants(tab_name)
    if history == 'y':
        table_history(tab_name)


def create_tablefile():
    pass


if __name__ == '__main__':
    #TODO könyvtár és fájl létrehozása, esetleg beírás a create_table.sql-be is
    params = gen_table_params
    repo = Repository(params['repo'])
    base = repo.get_base_path()
    tab_name = params['tablename'].lower()
    tab_short_name = params['table_shortname']
    history = params['history']
    url = params['url']
    db = repo.get_db_name()
    db_path = db.replace('-', '_')
    schema = repo.get_schema
    create_tablefile()
    tab_comment, table = get_table_from_confluence(tab_name, url)
    print_table_script(tab_comment, tab_name, table, history)

