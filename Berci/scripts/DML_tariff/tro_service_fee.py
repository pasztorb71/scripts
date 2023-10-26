
if __name__ == '__main__':
    table = 'tro_service_fee'
    postfix = '_1'
    with open('c:/Users/bertalan.pasztor/Downloads/Bali_launch_data/Bali_tro_service_fee_init_0.1.csv', 'r', encoding='utf8') as f:
        first_line = f.readline().strip()
        xid = 1
        print(f'INSERT INTO {table} (x__id, x__insuser, tro_id, lump_sum, lane_fee, number_of_lanes, validity_start, status, source) VALUES')
        for line in f.readlines()[0:]:
            arr = line.split(';')
            print(f"('{str(xid) + postfix}', '0', '{arr[0]}' ,'{arr[1].replace(' ','').replace(',','.')}', "
                  f"{arr[2].replace(' ','').replace(',','.')}, {arr[3].replace(',','.')}, "
                  f"to_date('{arr[4]}','DD.MM.YYYY'), '{arr[5]}', '{arr[6].strip()}'),")
            xid += 1