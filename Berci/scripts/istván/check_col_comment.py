#
def check_col_comment ( p_database , p_owner , p_table ):
    global path
    con = pg_connect( p_database )
    con=psycopg2.connect(
        host="127.0.0.1",
        port=5435,
        database=p_database,                # "core_customer",
        user="postgres",                    # "postgres"               / "dwh_read",
        password='fLXyFS0RpmIX9uxGII4N')  # "fLXyFS0RpmIX9uxGII4N" ) / 'mlffTitkosPassword123!')
    cursor=con.cursor()
    sql = "SELECT column_name, coalesce(col_description('" + p_owner + "." + p_table + "'::regclass, ordinal_position),' ') col_comment from information_schema.columns where table_schema = '" + p_owner + "' and table_name = '" + p_table + "' order by ordinal_position; "
#   print(sql)
    cursor.execute(sql)
    pg_cols = cursor.fetchall()
#
    for pg_col in pg_cols:
        if "dropped" not in pg_col[0]:
            line = pg_col[0]
            for i in range( len( line ) ):
                if ord( line[i:i+1] ) > 126:
                    print( line )
#
def check_col_comments():
    global database
    global owner
    global table
    global row_num
    if row_num == 0:
        read_milf_params()
    for i in range(row_num):
        check_col_comment( database[i] , owner[i] , table[i] )
#

