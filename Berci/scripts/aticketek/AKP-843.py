from dataclasses import dataclass

file = "C:/GIT/AKP/data-backend-database-postgres-liquibase/liquibase/masterdata/tables/traffic_calendar_day/data2.txt"

with open(file, 'r', encoding='utf-8') as f:
    for line in f:
        arr = line.strip().split(',')
        arr[1] = int(arr[1])
        arr[5] = 'null' if arr[5] == '' else f"'{arr[5]}'"
        arr[6] = 'null' if arr[6] == '' else f"'{arr[6]}'"
        print(f"('{arr[0]}', {arr[1]}, '{arr[2]}', '{arr[3]}', '{arr[4]}', {arr[5]}, {arr[6]}),")
        #break
