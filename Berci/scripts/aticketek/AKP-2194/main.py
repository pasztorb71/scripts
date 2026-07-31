from pprint import pprint

from classes.Database import Database


def get_tables(db):
    return [x[0] for x in db.sql_query("""SELECT table_name FROM information_schema.tables 
WHERE table_schema  = 'akp_masterdata'
AND table_name  NOT LIKE '%_p2%'
AND table_name NOT LIKE '%$his%'""")]


if __name__ == '__main__':
    db = Database(name='akp_be', host='10.255.0.112', password='mK6TqyF2sajRenJu53S7EB')
    tables = get_tables(db)
    for table in tables:
        #print(f"ALTER TABLE akp_masterdata.{table} ALTER COLUMN x__insdate SET DEFAULT (CURRENT_TIMESTAMP AT TIME ZONE 'UTC'::text);")
        print(f"CALL public.measurement_info_trigger_generator('akp_masterdata', '{table}');")




