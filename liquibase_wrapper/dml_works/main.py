def gen_delete_ids(fname):
    out = ''
    with open(fname, 'r', encoding='utf-8') as f:
        print('(', end='')
        cnt = 1
        for l in f.read().splitlines():
            id = l.split(',')[0].replace('(','').strip()
            out += id + ','
            if cnt % 7 ==0:
                out += '\n'
                cnt = 0;
            cnt += 1
    print(out[:-2]+"');", end='')


if __name__ == '__main__':
    gen_delete_ids('inserts.txt')