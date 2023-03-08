from datetime import datetime

if __name__ == '__main__':
    table1 = 'segment_revenue_share'
    table2 = 'revenue_share_percent'
    status = 'APPROVED'
    with open('c:/Users/bertalan.pasztor/Downloads/segment_revenue_share_init.csv', 'r', encoding='utf8') as f:
        table1_l = [f'INSERT INTO tro_clearing.segment_revenue_share (x__id, x__insuser, gli_segment_id, validity_start, status, source, supersegment) VALUES']
        table2_l = [f'INSERT INTO tro_clearing.revenue_share_percent (x__id, x__insuser, segment_revenue_share_id, tro_id, percentage) VALUES']
        for line in f.read().split('\n')[1:]:
            arr = line.split(';')
            gli_segment_id = arr[0]
            tro_id = arr[1]
            percentage = arr[2][:-1]
            validity_start = datetime.strptime(arr[3], '%d/%m/%Y').date()
            status = arr[4]
            supersegment = arr[5]
            source = arr[6]
            table1_l.append(f"('{gli_segment_id}', 0, '{gli_segment_id}' ,'{validity_start}', '{status}', '{source}', {supersegment}),")
            table2_l.append(f"('{gli_segment_id}', 0, '{gli_segment_id}' ,'{tro_id}', {percentage}),")
        print('\n'.join(table1_l)[:-1] + ';')
        print('\n'.join(table2_l)[:-1] + ';')


