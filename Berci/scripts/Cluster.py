import psycopg2 as psycopg2

import Environment


class Cluster:
    def __init__(self, port, passw, host='localhost'):
        self.host = host
        self.port = port
        self.passw = passw
        self.conn = psycopg2.connect(
            host=host,
            port=port,
            database="postgres",
            user="postgres",
            password=passw)

    @property
    def databases(self):
        cur = self.conn.cursor()
        cur.execute("SELECT datname from pg_database WHERE datistemplate IS FALSE AND datname NOT IN "
                    "('cloudsqladmin', 'postgres', 'sb-managed-db', 'sandbox', 'demo', 'payment_psp_clearing') ORDER BY datname")
        record = cur.fetchall()
        cur.close()
        return [rec[0] for rec in record]

    def db_command_all_db(self, stmt):
        pass

def cluster_selector() -> Cluster:
    print('Válassz instance-t!')
    for idx, instance in enumerate(Environment.offset):
        print(f'{idx}: {instance.split("-")[1]}')
    idx = int(input('Írd be a sorszámát:'))
    env_name = list(Environment.new_base.keys())[idx]
    return Env(env_name)

