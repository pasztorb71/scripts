import psycopg2

if __name__ == '__main__':
    dsn_src = "dbname=suppliers user=postgres password=postgres"
    with psycopg2.connect(dsn_src) as conn1, psycopg2.connect(dsn_tgt) as conn2:
        with conn1.cursor().copy("COPY src TO STDOUT (FORMAT BINARY)") as copy1:
            with conn2.cursor().copy("COPY tgt FROM STDIN (FORMAT BINARY)") as copy2:
                for data in copy1:
                    copy2.write(data)