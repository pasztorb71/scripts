
if __name__ == '__main__':
    table = 'tro'
    postfix = '_1'
    with open('c:/Users/bertalan.pasztor/Downloads/Bali_launch_data/Bali_tro_init_0.1.csv', 'r',
              encoding='utf8') as f:
        tro_l = [(f'INSERT INTO {table} (x__id, x__insuser, name, gli_tro_id) VALUES')]
        for line in f.read().split('\n')[1:]:
            if line == '': continue
            arr = line.split(';')
            tro_l.append(f"('{arr[0]}', '0', '{arr[1]}' ,'{arr[0]}'),")
        print('\n'.join(tro_l)[:-1] + ';')