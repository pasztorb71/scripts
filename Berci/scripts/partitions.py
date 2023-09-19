import datetime

from dateutil.utils import today

import Database
import Environment
from utils.utils_sec import password_from_file


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(days=n)


def get_record_per_days_from_table(db, schema_table, partkey):
    print(f'-- Counting records in table... ({schema_table})')
    cmd = f"select {partkey}::date, count(*) from {schema_table} GROUP BY 1 ORDER BY 1;"
    print(cmd)
    res = db.sql_query(f"select {partkey}::date, count(*) from {schema_table} GROUP BY 1 ORDER BY 1;")
    return [[str(x[0]), str(x[1])] for x in res]

def add_n_days(datestring: str, days: int) -> str:
    # convert the string to a datetime object with timezone information
    date = datetime.datetime.fromisoformat(datestring)

    # add one day to the timestamp
    new_date = date + datetime.timedelta(days=1)

    # convert the new timestamp back to a string in the same format
    return new_date.strftime("%Y-%m-%d")


def list_days_in_default(days):
    for day in days:
        print(f"{day[0].replace('-', '_')} {day[1]}")
    print()

def pr_create_partition_of_table(days, schema_table):
    for day in days:
        print(f"""CREATE TABLE {schema_table}_p{day[0].replace('-', '_')} PARTITION OF {schema_table}
    FOR VALUES FROM ('{day[0]}') TO ('{add_n_days(day[0], 1)}');""")
    print()
    #FOR VALUES FROM ('{day[0]} 02:00:00+02:00') TO ('{add_n_days(day[0], 1)} 02:00:00+02:00');""")


def pr_create_table_like_multiple_days(days, schema_table):
    for day in days:
        pr_create_table_like(day, schema_table)
    print()


def pr_create_table_like(day, schema_table):
    print(f"CREATE TABLE {schema_table}_p{day.replace('-', '_')} (LIKE {schema_table});")


def pr_create_single_partitions(day, schema_table):
    print(f"CREATE TABLE {schema_table}_p{day[0].replace('-', '_')} (LIKE {schema_table});")
    print()

def pr_create_future_partitions(days, schema_table):
    print('--future partitions')
    if days:
        start_date = datetime.datetime.strptime(days[-1][0], '%Y-%m-%d') + datetime.timedelta(days=1)
    else:
        start_date = today()
    end_date = today() + datetime.timedelta(days=10)
    for day in daterange(start_date, end_date):
        day_str = day.strftime('%Y_%m_%d')
        nexday_str = add_n_days(day_str.replace('_','-'), 1)
        print(f"CREATE TABLE {schema_table}_p{day_str} PARTITION OF {schema_table} "
              f"FOR VALUES FROM ('{day_str.replace('_','-')} 01:00:00+01') TO ('{nexday_str} 01:00:00+01');")
    print()

def pr_insert_partitions(days, schema_table, new_schema_table):
    for day in days:
        pr_insert_single_partition(day, schema_table, new_schema_table)
    print()

def pr_insert_single_partition(day, schema_table, new_schema_table):
    print(f"""INSERT INTO {new_schema_table}_p{day.replace('-', '_')}
  SELECT * FROM {schema_table}
  WHERE {partkey} >= '{day} 02:00:00+02:00' AND {partkey} < '{add_n_days(day, 1)} 02:00:00+02:00';""")

def pr_count_part_records_multiple_days(days, schema_table):
    for day in days:
        pr_count_part_records(day, schema_table)
    print()

def pr_count_part_records(day, schema_table):
    print(f"""select '{schema_table.split('.')[1]}_p{day.replace('-', '_')}' as day, count(*) from {schema_table}_p{day.replace('-', '_')};""")

def pr_count_records(schema_table):
    print(f"SELECT COUNT(*) FROM {schema_table};")
    print()

def pr_count_default_ranges(days, schema_table):
    for day in days:
        print(f"""SELECT count(*) FROM {schema_table}_default
                      WHERE {partkey} >= '{day[0]} 01:00:00+01:00' AND {partkey} < '{add_n_days(day[0], 1)} 01:00:00+01:00';""")
    print()

def pr_count_single_default_ranges(day, schema_table):
    print(f"""SELECT count(*) FROM {schema_table}_default
                  WHERE {partkey} >= '{day[0]} 01:00:00+01:00' AND {partkey} < '{add_n_days(day[0], 1)} 01:00:00+01:00';""")
    print()

def pr_delete_partitions(days, schema_table):
    for day in days:
        pr_delete_single_partition(day, schema_table)
    print()


def pr_delete_single_partition(day, schema_table):
    print(f"""DELETE FROM {schema_table}_default
  WHERE {partkey} >= '{day} 02:00:00+02:00' AND {partkey} < '{add_n_days(day, 1)} 02:00:00+02:00';""")


def pr_attach_partitions_multiple_days(days, schema_table):
    for day in days:
        pr_attach_partition(day, schema_table)
    print()


def pr_attach_partition(day, schema_table):
    print(f"""ALTER TABLE {schema_table} ATTACH PARTITION {schema_table}_p{day.replace('-', '_')}
  FOR VALUES FROM ('{day} 02:00:00+02:00') TO ('{add_n_days(day, 1)} 02:00:00+02:00');""")

def remove_default_part_data(db, schema_table, partkey):
    print(get_login_str(db))
    days_records_all = get_record_per_days_from_table(db, schema_table+'_default', partkey)
    list_days_in_default(days_records_all)
    days = [d[0] for d in days_records_all]
    for day in days:
        print(f'-- {day} ---')
        print('begin transaction;')
        pr_create_table_like(day, schema_table)
        pr_insert_single_partition(day, schema_table+'_default', schema_table)
        pr_count_part_records(day, schema_table)
        pr_delete_single_partition(day, schema_table)
        pr_attach_partition(day, schema_table)
        print('commit;')
        print(f'-- End of {day} ---\n\n')


def get_login_str(db):
    return f"""@SET PGPASSWORD={password_from_file('postgres', db.port)}
psql -p {db.port} -U postgres -d {db.name}
"""


def check_eligibility_partitions_in_all_env():
    for env in Environment.get_envs(exclude=['local'])[0:1]:
        print(Environment.Env(env).get_ports())
        #TODO check_default_partitions
        #check_default_partitions()


def partgen(db, schema_table, partkey):
    new_schema_table = schema_table.replace('_old','')
    print(get_login_str(db))
    days_records = get_record_per_days_from_table(db, schema_table, partkey)
    list_days_in_default(days_records)
    #operations_by_partition(days_records, new_schema_table, schema_table)
    operations_by_type(days_records, new_schema_table, schema_table)


def pr_insert_select(schema_table, new_schema_table):
    print(f"INSERT INTO {new_schema_table} SELECT * FROM {schema_table};")
    print()


def operations_by_type(days_records, new_schema_table, schema_table):
    #pr_create_table_like(days_records, new_schema_table)
    # pr_create_future_partitions(days_records, schema_table)
    pr_create_partition_of_table(days_records, new_schema_table)
    pr_insert_select(schema_table, new_schema_table)
    pr_count_records(schema_table)
    pr_count_records(new_schema_table)
    #pr_insert_partitions(days_records, schema_table, new_schema_table)
    #pr_count_part_records(days_records, new_schema_table)
    #pr_delete_partitions(days_records, schema_table)
    # print(f"select count(*) from {schema_table}_default;")
    #pr_attach_partitions(days_records, new_schema_table)


def operations_by_partition(days_records, new_schema_table, schema_table):
    for day in days_records:
        print(f'-- {day[0]} ---')
        print('begin transaction;')
        pr_create_single_partitions(day, new_schema_table)
        pr_insert_single_partition(day, schema_table, new_schema_table)
        # pr_count_single_default_ranges(day, schema_table)
        # pr_delete_single_default_partitions(day, schema_table)
        pr_attach_partition(day, new_schema_table)
        print('commit;')
        print(f'-- End of {day[0]} ---\n\n')
    print('-- End of single operations\n')


if __name__ == '__main__':
    port = Environment.Env('cantas_test').get_port_from_inst('pg-enforcement')
    db = Database.Database('enforcement_eligibility', port)
    partkey = 'event_time'
    #TODO átírni objektumosra
    #partgen(db, 'payment_transaction.payment_transaction_old', partkey)
    remove_default_part_data(db, 'eligibility.detection_data', partkey)
    #check_eligibility_partitions_in_all_env()

