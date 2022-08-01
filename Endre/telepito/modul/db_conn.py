import sqlite3
from sqlite3 import Error


def sqlite_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_table(db_file):
    sql = """ CREATE TABLE IF NOT EXISTS database_changeset (
                    pk_id integer,
                    author text,
                    changeset_id text,
                    run_on_change integer,
                    comment text,
                    precond_on_fail text,
                    precond_on_error text,
                    precond_expected_res_num integer,
                    precond_sql_check_text text,
                    PRIMARY KEY("pk_id" AUTOINCREMENT  ) """

    conn = sqlite_connection(db_file)
    with conn:
        c = conn.cursor()
        c.execute(sql)


def insert_table():
    conn = sqlite_connection(db_file)
    sql = ''' INSERT INTO tasks(name,priority,status_id,project_id,begin_date,end_date)
                  VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    return cur.lastrowid


if __name__ == '__main__':
    create_table(r"C:\sqlite\db\pythonsqlite.db")
