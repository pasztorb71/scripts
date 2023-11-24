
with open('c:/Users/bertalan.pasztor/Downloads/phone_number_whitelist - Sheet1.csv', 'r') as f:
    cnt = 1
    for nr in f.read().split('\n')[1:]:
        print(f"""INSERT INTO phone_number_whitelist (x__id, x__insuser, x__moddate, x__moduser, x__version, phone_number)
    VALUES('TEST{str(cnt)}', 'test', NULL, NULL, 0, '{nr}') ON CONFLICT DO NOTHING;""")
        cnt += 1
