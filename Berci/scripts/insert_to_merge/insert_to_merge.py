insert = '''INSERT INTO test
(x__id, x__insdate, x__insuser, x__moddate, x__moduser, x__version, "year", closed, approved, calendar_structure_complete)
VALUES('2026', '2026-01-20 12:03:27.630', '0', NULL, NULL, 0, 2026, false, false, false);'''


def generate_merge_from_insert(insert) -> str:
    # create the merge command using the insert command
    # extract the table name
    table_name = insert.split()[2]
    # extract the columns and values
    columns = insert.split('(')[1].split(')')[0].split(', ')
    values = insert.split('VALUES(')[1].split(')')[0].split(', ')
    # if column name is in ('x__insdate', 'x__moddate') then the values = values::timestamp
    values = [f"{value}::timestamp" if col in ('x__insdate', 'x__moddate') else value for col, value in zip(columns, values)]
    # create the merge command
    merge_command = f'''MERGE INTO {table_name} 
USING ( 
    SELECT {", ".join(values)}) 
    AS tmp ({", ".join(columns)}) 
ON (tmp.x__id = {table_name}.x__id) 
WHEN NOT MATCHED THEN 
INSERT ({", ".join(columns)}) 
VALUES ({", ".join([f"tmp.{col}" for col in columns])});'''
    return merge_command

if __name__ == '__main__':
    tables = ['traffic_calendar_year',
              'traffic_calendar_month',
              'traffic_calendar_week',
              'traffic_calendar_day',
              #'periodicity_factor_traffic_time_profile',
              #'periodicity_factor_veh_grp_x_traf_time_prof_map'
              ]

    for table in tables:
        print(f'Generating merge command for {table}...')
        with open(f'{table}_insert.sql', 'r', encoding='utf-8') as f:
            with open(f'{table}_merge.sql', 'w') as f_out:
                for insert in f.read().split(';\n'):
                    merge_command = generate_merge_from_insert(insert) + '\n'
                    f_out.write(merge_command)
