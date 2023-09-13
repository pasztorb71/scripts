import psycopg2

from utils import utils_sec
from Cluster import Cluster
from Environment import get_port_from_env_repo


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
        for i in range(len(keys1)):
            if keys1[i] != keys2[i]:
                print("Constraints does not match for table {}".format(keys1[i][1]))
                print(keys1[i])
                print(keys2[i])

def ck(conn1, conn2):
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cmd = f"""select pgc.conname as constraint_name,
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
        for i in range(len(keys1)):
            if keys1[i] != keys2[i]:
                print("Check constraints does not match for table {}".format(keys1[i][0]))
                print(keys1[i])
                print(keys2[i])


def indexes(conn1, conn2):
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    cmd = f"SELECT * FROM pg_catalog.pg_indexes WHERE schemaname NOT IN ('pg_catalog', 'public') order by 1,2,3,5"
    cur1.execute(cmd)
    keys1 = cur1.fetchall()
    cur2.execute(cmd)
    keys2 = cur2.fetchall()

    if len(keys1) != len(keys2):
        print("Number of indexes does not match between the two databases")
        print('1', set(keys1) - set(keys2))
        print('2', set(keys2) - set(keys1))
    else:
        for i in range(len(keys1)):
            if keys1[i] != keys2[i]:
                print("indexes does not match for table {}".format(keys1[i][1]))
                print(keys1[i])
                print(keys2[i])

def compare(dbname):
    print(dbname)
    port = get_port_from_env_repo('fit')
    database = dbname
    conn1 = psycopg2.connect(f"host=localhost port={port} dbname={database} "
                             f"user=postgres password={utils_sec.password_from_file('postgres', 'localhost', port)}")
    port = get_port_from_env_repo('test')
    database = dbname
    conn2 = psycopg2.connect(f"host=localhost port={port} dbname={database} "
                             f"user=postgres password={utils_sec.password_from_file('postgres', 'localhost', port)}")
    cur1 = conn1.cursor()
    cur2 = conn2.cursor()
    # Query the table structure from both databases
    cur1.execute(
        f"SELECT table_schema, table_name, column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_schema not in "
        f"('public', 'information_schema') and table_schema not like 'pg_%' order by 1,2,3")
    tables1 = cur1.fetchall()
    cur2.execute(
        f"SELECT table_schema, table_name, column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_schema not in "
        f"('public', 'information_schema') and table_schema not like 'pg_%' order by 1,2,3")
    tables2 = cur2.fetchall()
    # Compare the table structure between the two databases
    if len(tables1) != len(tables2):
        print("Number of tables does not match between the two databases")
        print('1', set(tables1) - set(tables2))
        print('2', set(tables2) - set(tables1))
    else:
        for i in range(len(tables1)):
            if tables1[i] != tables2[i]:
                print("Table structure does not match for table {}".format(tables1[i][1]))
    pk_fk(conn1, conn2)
    ck(conn1, conn2)
    indexes(conn1, conn2)
    cur1.close()
    cur2.close()
    conn1.close()
    conn2.close()


if __name__ == '__main__':
    host, port = 'localhost', get_port_from_env_repo('test')
    cluster = Cluster(host=host, port=port, passw=utils_sec.password_from_file('postgres', host, port))
    databases = cluster.databases[0:]
    for db in databases:
        compare(db)