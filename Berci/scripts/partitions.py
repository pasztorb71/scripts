import datetime
from time import strftime

from dateutil.utils import today

import Database
import utils
from docker_ips import new_base


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + datetime.timedelta(days=n)


def get_record_per_days_from_table(db, schema_table):
    print(f'-- Counting records in default partition... ({schema_table})')
    res = db.sql_query(f"select {partkey}::date, count(*) from {schema_table}_default GROUP BY 1 ORDER BY 1;")
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


def pr_create_partitions(days, schema_table):
    for day in days:
        print(f"CREATE TABLE {schema_table}_p{day[0].replace('-', '_')} (LIKE {schema_table});")
    print()

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

def pr_insert_partitions(days, schema_table):
    for day in days:
        print(f"""INSERT INTO {schema_table}_p{day[0].replace('-', '_')}
                    SELECT * FROM {schema_table}_default
                      WHERE {partkey} >= '{day[0]} 01:00:00+01:00' AND {partkey} < '{add_n_days(day[0], 1)} 01:00:00+01:00';""")
    print()


def pr_insert_single_partitions(day, schema_table):
    print(f"""INSERT INTO {schema_table}_p{day[0].replace('-', '_')}
                SELECT * FROM {schema_table}_default
                  WHERE {partkey} >= '{day[0]} 01:00:00+01:00' AND {partkey} < '{add_n_days(day[0], 1)} 01:00:00+01:00';""")
    print()


def pr_count_part_records(days, schema_table):
    for day in days:
        print(
            f"""select '{schema_table.split('.')[1]}a_p{day[0].replace('-', '_')}' as day, count(*) from {schema_table}_p{day[0].replace('-', '_')}
union all""")
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

def pr_delete_default_partitions(days, schema_table):
    for day in days:
        print(f"""DELETE FROM {schema_table}_default
  WHERE {partkey} >= '{day[0]} 01:00:00+01:00' AND {partkey} < '{add_n_days(day[0], 1)} 01:00:00+01:00';""")
    print()


def pr_delete_single_default_partitions(day, schema_table):
    print(f"""DELETE FROM {schema_table}_default
  WHERE {partkey} >= '{day[0]} 01:00:00+01:00' AND {partkey} < '{add_n_days(day[0], 1)} 01:00:00+01:00';""")
    print()


def pr_attach_partitions(days, schema_table):
    for day in days:
        print(f"""ALTER TABLE {schema_table} ATTACH PARTITION {schema_table}_p{day[0].replace('-', '_')}
  FOR VALUES FROM ('{day[0]} 01:00:00+01:00') TO ('{add_n_days(day[0], 1)} 01:00:00+01:00');""")
    print()


def pr_attach_single_partitions(day, schema_table):
    print(f"""ALTER TABLE {schema_table} ATTACH PARTITION {schema_table}_p{day[0].replace('-', '_')}
  FOR VALUES FROM ('{day[0]} 01:00:00+01:00') TO ('{add_n_days(day[0], 1)} 01:00:00+01:00');""")
    print()


def remove_default_part_data(port, schema_table):
    db = Database.Database('enforcement_eligibility', 'localhost', port)
    print(f"""@SET PGPASSWORD={utils.password_from_file('postgres', port)}
psql -p {db.port} -U postgres -d {db.name}
""")
    days_records = get_record_per_days_from_table(db, schema_table)
    list_days_in_default(days_records)
    for day in days_records:
        print(f'-- {day[0]} ---')
        print('begin transaction;')
        pr_create_single_partitions(day, schema_table)
        pr_insert_single_partitions(day, schema_table)
        pr_count_single_default_ranges(day, schema_table)
        pr_delete_single_default_partitions(day, schema_table)
        pr_attach_single_partitions(day, schema_table)
        print('commit;')
        print(f'-- End of {day[0]} ---\n\n')
    print('-- End of single operations\n')
    pr_create_partitions(days_records, schema_table)
    pr_create_future_partitions(days_records, schema_table)
    pr_insert_partitions(days_records, schema_table)
    # pr_count_part_records(days_records, schema_table)
    pr_count_default_ranges(days_records, schema_table)
    pr_delete_default_partitions(days_records, schema_table)
    # print(f"select count(*) from {schema_table}_default;")
    print()
    pr_attach_partitions(days_records, schema_table)


def check_default_partitions():
    pass


def check_eligibility_partitions_in_all_env():
    for env in utils.get_envs(exclude=['local'])[0:1]:
        print(utils.get_ports_from_env(env))
        #check_default_partitions()


if __name__ == '__main__':
    partkey = 'event_time'
    port = utils.get_port_from_env_inst('test', 'pg-enforcement')
    remove_default_part_data(port, 'eligibility.detection_minilog_record')
    #check_eligibility_partitions_in_all_env()

