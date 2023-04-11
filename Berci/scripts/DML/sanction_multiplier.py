
if __name__ == '__main__':
    table = 'sanction_multiplier'
    postfix = '_1'
    with open('c:/Users/bertalan.pasztor/Downloads/sanction_multiplier_init_data.csv', 'r', encoding='utf8') as f:
        first_line = f.readline().strip()
        xid = 0
        print('TRUNCATE TABLE sanction_multiplier;')
        print(f'INSERT INTO {table} (x__id, x__insuser, segment_id, gli_segment_id, multiplier_level_1, waiting_level_1, multiplier_level_2, waiting_level_2, multiplier_level_3, waiting_level_3, validity_start, validity_end, source, sanction_multiplier_upload_id) VALUES')
        for line in f.readlines()[0:]:
            arr = line.split(';')
            print(f"('{str(xid) + postfix} ', '0', '{arr[0] + postfix}' ,'{arr[0]}', {arr[1]}, {arr[2]}, {arr[3]}, {arr[4]}, {arr[5]}, {arr[6].strip()}, '2022-01-01', null, 'MAP_LOAD', null),")
            xid += 1