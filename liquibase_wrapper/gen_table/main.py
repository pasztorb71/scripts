import math

import pandas as pd

from liquibase_wrapper.gen_table.Confluence import Confluence



def modify_type(col):
    return col.lower().replace('varchar2', 'varchar')\
        .replace('timestamp_with_timezone', 'timestamptz(6)')\
        .replace('decimal', 'numeric')\
        .replace('smallint', 'int2').replace('blob', 'bytea')


def get_table_from_confluence(table, url):
    conf = Confluence()
    html = conf.get_table_from_url(url)
    table_comment = conf.get_table_comment()
    tab = pd.read_html(html)
    df = tab[0]
    a = list(df.columns)
    return table_comment, [list(df.columns)] + df.values.tolist()


def table_columns(tab_name, table):
    header = "CREATE TABLE " + tab_name + " (" + \
             "\n\tx__id varchar(30) NOT NULL," \
             "\n\tx__insdate timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP," \
             "\n\tx__insuser varchar(30) NOT NULL," \
             "\n\tx__moddate timestamptz(6) NULL," \
             "\n\tx__moduser varchar(30) NULL," \
             "\n\tx__version int8 NOT NULL DEFAULT 0,"
    print(header)
    colnames = table[0]
    a = [row for row in table if not row[0].lower().startswith('x__')][1:]
    for col in [row for row in table if not row[0].lower().startswith('x__')][1:]:
        if colnames[3] == 'DEFAULT':
            default = ' DEFAULT ' + str(col[3]).lower() if not math.isnan(col[3]) else ''
            null = ' NULL' if col[2].lower() == 'nullable' else ' NOT NULL'
        else:
            default = ' DEFAULT ' + str(col[2]).lower() if not math.isnan(col[2]) else ''
            null = ' NULL' if col[3].lower() == 'nullable' else ' NOT NULL'
        type = modify_type(col[1])
        print('\t' + col[0].lower() + ' ' + type + null + default + ',')
    print('\t' + 'CONSTRAINT pk_' + tab_name.split('.')[1] + ' PRIMARY KEY (x__id)\n);')

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
    for col in [row for row in table if not row[0].lower().startswith('x__')][1:]:
        print('COMMENT ON COLUMN ' + tab_name + "." + col[0].lower() + " IS '" + col[4] + "';")


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

ALTER TABLE !sema!.!table! OWNER TO ${schema_name_!sema!}_tbl_own;

GRANT SELECT ON TABLE !sema!.!table! TO ${schema_name_!sema!}_sel;
GRANT INSERT, UPDATE ON TABLE !sema!.!table! TO ${schema_name_!sema!}_mod;
GRANT DELETE, TRUNCATE ON TABLE !sema!.!table! TO ${schema_name_!sema!}_del;

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


def print_table_script(tab_comment, tab_name, table):
    print('--liquibase formatted sql\n')
    table_header(tab_name)
    table_columns(tab_name, table)
    print()
    table_comments(tab_comment, tab_name, table)
    print()
    table_grants(tab_name)


if __name__ == '__main__':
    tab_name = 'eobu_tariff.SEGMENT_TARIFF'.lower()
    url = 'https://confluence.icellmobilsoft.hu/display/MLFF/SEGMENT_TARIFF'
    tab_comment, table = get_table_from_confluence(tab_name, url)
    print_table_script(tab_comment, tab_name, table)

