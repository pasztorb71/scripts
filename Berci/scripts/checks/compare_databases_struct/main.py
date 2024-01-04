import logging

import Environment
from Database import Database
from checks.compare_databases_struct.databases import Metadb
from utils import utils_sec

def comp_columns(conn1, conn2):
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cmd = f"SELECT " \
          f"table_schema,table_name,column_name,column_default,is_nullable,data_type,character_maximum_length,character_octet_length,numeric_precision " \
          f"FROM information_schema.columns " \
          f"WHERE table_name NOT LIKE '%_p%' " \
          f"ORDER BY table_schema, table_name, column_name"
    cur1.execute(cmd)
    keys1 = cur1.fetchall()
    cur2.execute(cmd)
    keys2 = cur2.fetchall()

    if len(keys1) != len(keys2):
        print("Number of columns does not match between the two databases")
        print('1', set(keys1) - set(keys2))
        print('2', set(keys2) - set(keys1))
    else:
        print("Number of columns :OK")
        is_column_diff = False
        for i in range(len(keys1)):
            if keys1[i] != keys2[i]:
                print("column does not match for table {}".format(keys1[i][1]))
                print(keys1[i])
                print(keys2[i])
                is_column_diff = True
        if is_column_diff == False:
            print("Column structure: OK")

def pk_fk(conn1, conn2):
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cmd = f"""SELECT * FROM (
SELECT
    pgc.contype as constraint_type,
    pgc.conname as constraint_name,
    ccu.table_schema AS table_schema,
    kcu.table_name as table_name,
    CASE WHEN (pgc.contype = 'f') THEN kcu.COLUMN_NAME ELSE ccu.COLUMN_NAME END as column_name, 
    CASE WHEN (pgc.contype = 'f') THEN ccu.TABLE_NAME ELSE (null) END as reference_table,
    CASE WHEN (pgc.contype = 'f') THEN ccu.COLUMN_NAME ELSE (null) END as reference_col,
    CASE WHEN (pgc.contype = 'p') THEN 'yes' ELSE 'no' END as auto_inc,
    CASE WHEN (pgc.contype = 'p') THEN 'NO' ELSE 'YES' END as is_nullable,
        'integer' as data_type,
        '0' as numeric_scale,
        '32' as numeric_precision
FROM
    pg_constraint AS pgc
    JOIN pg_namespace nsp ON nsp.oid = pgc.connamespace
    JOIN pg_class cls ON pgc.conrelid = cls.oid
    JOIN information_schema.key_column_usage kcu ON kcu.constraint_name = pgc.conname
    LEFT JOIN information_schema.constraint_column_usage ccu ON pgc.conname = ccu.CONSTRAINT_NAME 
    AND nsp.nspname = ccu.CONSTRAINT_SCHEMA
  UNION
     SELECT  null as constraint_type , null as constraint_name , 'public' as "table_schema" ,
    table_name , column_name, null as refrence_table , null as refrence_col , 'no' as auto_inc ,
    is_nullable , data_type, numeric_scale , numeric_precision
    FROM information_schema.columns cols 
    Where 1=1
    AND table_schema = 'public'
    and column_name not in(
        SELECT CASE WHEN (pgc.contype = 'f') THEN kcu.COLUMN_NAME ELSE kcu.COLUMN_NAME END 
        FROM
        pg_constraint AS pgc
        JOIN pg_namespace nsp ON nsp.oid = pgc.connamespace
        JOIN pg_class cls ON pgc.conrelid = cls.oid
        JOIN information_schema.key_column_usage kcu ON kcu.constraint_name = pgc.conname
        LEFT JOIN information_schema.constraint_column_usage ccu ON pgc.conname = ccu.CONSTRAINT_NAME 
        AND nsp.nspname = ccu.CONSTRAINT_SCHEMA
    )
)   as foo
WHERE constraint_name NOT LIKE 'pg_%'
AND table_schema NOT IN ('ddl_changes', 'public')
AND table_name NOT LIKE '%_p%'
AND reference_table NOT LIKE '%_p%'
ORDER BY table_schema , table_name, constraint_name, column_name DESC"""
    cur1.execute(cmd)
    keys1 = cur1.fetchall()
    cur2.execute(cmd)
    keys2 = cur2.fetchall()

    if len(keys1) != len(keys2):
        print("Number of fk_pk does not match between the two databases")
        print('1', set(keys1) - set(keys2))
        print('2', set(keys2) - set(keys1))
    else:
        print("Number of fk_pk :OK")
        is_pkfk_diff = False
        for i in range(len(keys1)):
            if keys1[i] != keys2[i]:
                print("Constraints does not match for table {}".format(keys1[i][1]))
                print(keys1[i])
                print(keys2[i])
                is_pkfk_diff = True
        if is_pkfk_diff == False:
            print("pk_fk structure: OK")

def ck(conn1, conn2):
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cmd = f"""select distinct pgc.conname as constraint_name,
       ccu.table_schema as table_schema,
       ccu.table_name,
       ccu.column_name,
       pg_get_constraintdef(pgc.oid) as definition
from pg_catalog.pg_constraint pgc
join pg_namespace nsp on nsp.oid = pgc.connamespace
join pg_class  cls on pgc.conrelid = cls.oid
left join information_schema.constraint_column_usage ccu
          on pgc.conname = ccu.constraint_name
          and nsp.nspname = ccu.constraint_schema
where contype ='c'
AND table_name NOT LIKE '%_p%'
order by table_schema , table_name, constraint_name, column_name"""
    cur1.execute(cmd)
    keys1 = cur1.fetchall()
    cur2.execute(cmd)
    keys2 = cur2.fetchall()

    if len(keys1) != len(keys2):
        print("Number of cks does not match between the two databases")
        print('1', set(keys1) - set(keys2))
        print('2', set(keys2) - set(keys1))
    else:
        print("Number of cks: OK")
        is_ckstruct_diff = False
        for i in range(len(keys1)):
            if keys1[i] != keys2[i]:
                print("Check constraints does not match for table {}".format(keys1[i][0]))
                print(keys1[i])
                print(keys2[i])
                is_ckstruct_diff = True
        if is_ckstruct_diff == False:
            print("Check constraints: OK")

def indexes(conn1, conn2):
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cmd = f"SELECT " \
          f"schemaname, " \
          f"tablename, " \
          f"indexname, " \
          f"REPLACE(indexdef, ' ONLY ', ' ')  " \
          f"FROM pg_catalog.pg_indexes WHERE schemaname NOT IN ('pg_catalog', 'public') " \
          f"AND tablename NOT LIKE '%_p%' " \
          f"order by 1,2,3,4"
    cur1.execute(cmd)
    keys1 = cur1.fetchall()
    cur2.execute(cmd)
    keys2 = cur2.fetchall()

    if len(keys1) != len(keys2):
        print("Number of indexes does not match between the two databases")
        print('1', set(keys1) - set(keys2))
        print('2', set(keys2) - set(keys1))
    else:
        print("Number of indexes: OK")
        is_indexes_diff = False
        for i in range(len(keys1)):
            if keys1[i] != keys2[i]:
                print("indexes does not match for table {}".format(keys1[i][1]))
                print(keys1[i])
                print(keys2[i])
                is_indexes_diff = True
        if is_indexes_diff == False:
            print("Indexes: OK")

def compare(dblist1: list[Database], dblist2: list[Database]):
    compare_database_names(dblist1, dblist2)
    tables1 = [x for x in db1.tables if '_p' not in x]
    tables2 = [x for x in db2.tables if '_p' not in x]
    # Compare the table structure between the two databases
    if len(tables1) != len(tables2):
        print("Number of tables does not match between the two databases")
        print('1', set(tables1) - set(tables2))
        print('2', set(tables2) - set(tables1))
    else:
        print("Number of tables : OK")
        is_tablestruct_diff = False
        for i in range(len(tables1)):
            if tables1[i] != tables2[i]:
                print("Table structure does not match for table {}".format(tables1[i][1]))
                is_tablestruct_diff = True
        if is_tablestruct_diff == False:
            print("Table structures: OK")
    comp_columns(db1.conn, db2.conn)
    pk_fk(db1.conn, db2.conn)
    ck(db1.conn, db2.conn)
    indexes(db1.conn, db2.conn)


def compare_database_names(dblist1, dblist2):
    dbnames1 = sorted([db.name for db in dblist1])
    dbnames2 = sorted([db.name for db in dblist2])
    if dbnames1 == dbnames2:
        logging.info('A két környezet egyező adatbázisneveket tartalmaz')
    else:
        logging.warning('1. Körnezet adatbázisai:')
        logging.warning(dbnames1)
        logging.warning('2. Körnezet adatbázisai:')
        logging.warning(dbnames2)


def get_databases_from_envs(envs: list[str], reload=False):
    dblist = {}
    for env in envs:
        dblist[env] = Environment.Env(env).databases
    return dblist


def read_databases_from_env(envlist: list[str], metadb: Metadb, reload=False):
    if reload == True:
        dblist = get_databases_from_envs(envlist)
        write_databases_to_metadb(metadb, dblist)
    else:
        read_databases_from_metadb(metadb)
    return dblist

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(levelname)s %(asctime)s - %(message)s")
    metadb = Metadb('C:\sqlite\mlffmeta.db')
    dblist1 = read_databases_from_env(['sandbox', 'prod'], metadb, reload=True)
    #compare(dblist1, dblist2)
    exit(0)
    host, port = 'localhost', get_port_from_env('test')
    cluster = Cluster(host=host, port=port, passw=utils_sec.password_from_file('postgres', host, port))
    databases = cluster.databases[0:]
    for db in databases:
        compare(db)