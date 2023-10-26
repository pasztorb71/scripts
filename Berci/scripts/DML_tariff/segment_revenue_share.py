from datetime import datetime

from DML_tariff.date import VALIDITY_START

if __name__ == '__main__':
    table1 = 'segment_revenue_share'
    table2 = 'revenue_share_percent'
    status = 'APPROVED'
    postfix = '_1'
    with open('c:/Users/bertalan.pasztor/Downloads/Bali_launch_data/Bali_segment_revenue_share_init.csv', 'r', encoding='utf8') as f:
        table1_l = [f'INSERT INTO segment_revenue_share (x__id, x__insuser, gli_segment_id, validity_start, status, source, supersegment) VALUES']
        table2_l = [f'INSERT INTO revenue_share_percent (x__id, x__insuser, segment_revenue_share_id, tro_id, percentage) VALUES']
        revshare_xid = 0
        revshareperc_xid = 0
        old_gli_segment_id = ''
        for line in f.read().split('\n')[1:]:
            if line == '': continue
            arr = line.split(';')
            gli_segment_id = arr[0]
            tro_id = arr[1]
            percentage = arr[2][:-1]
            status = arr[4]
            supersegment = arr[5]
            source = arr[6]
            if gli_segment_id != old_gli_segment_id:
                revshare_xid += 1
                table1_l.append(f"('{str(revshare_xid) + postfix}', 0, '{gli_segment_id}' ,{VALIDITY_START}, '{status}', '{source}', {supersegment}),")
                table2_l.append(f"('{str(revshareperc_xid) + postfix}', 0, '{str(revshare_xid) + postfix}' ,'{tro_id}', {percentage}),")
                revshareperc_xid += 1
                old_gli_segment_id = gli_segment_id
            else:
                table2_l.append(f"('{str(revshareperc_xid) + postfix}', 0, '{str(revshare_xid) + postfix}' ,'{tro_id}', {percentage}),")
                revshareperc_xid += 1
        print('\n'.join(table1_l)[:-1] + ';')
        print('\n'.join(table2_l)[:-1] + ';')


