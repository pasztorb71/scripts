import psycopg2

import Repository
import utils_db
from Cluster import Cluster
from Database import Database
from utils_sec import password_from_file


class Env():
    new_base = {'local': 5432,
                'sandbox': 5440,
                'dev': 5540,
                'fit': 5640,
                'cantas_train': 5740,
                'cantas_test': 5840,
                'perf': 5940,
                'cantas_dev': 6040
                }

    offset = {'pg-doc': 0,
              'pg-core': 1,
              'pg-enforcement': 2,
              'pg-eobu': 3,
              'pg-payment': 4,
              'pg-settlement': 5,
              # 'pg-data': 6,
              'pg-obu': 7,
              }

    def __init__(self, name='local'):
        self.name = name

    @property
    def database_names(self):
        names = []
        for port in self.get_ports(self.name):
            db = Database('postgres', 'localhost', str(port))
            rows = db.sql_query("SELECT datname from pg_database WHERE datistemplate IS FALSE "
                                "AND datname NOT IN ('cloudsqladmin', 'postgres')")
            names += [x[0] for x in rows]
        return names

    def get_port_from_inst(self, inst):
        if self.name in self.new_base:
            if inst in self.offset:
                return self.new_base[self.name] + self.offset[inst]
            else:
                print("Lehetséges instance-ok:")
                print('\n'.join([x for x in self.offset.keys()]))
                raise Exception("Nem létező instance")
        else:
            print(f"utils.get_port_from_env_inst('{self.name}')\n" + """"Nem létező környezet:
        Lehetséges értékek:
          sandbox
          dev
          fit
          perf
          train
          test
          new_""")
            raise Exception("Nem létező környezet")

    def get_ports(self) -> list[int]:
        if self.name == 'local':
            return [5432]
        ports = []
        for idx in self.offset.values():
            ports.append(self.new_base[self.name] + idx)
        return ports

    def get_port_from_repo(self, repo_full_name: str) -> int:
        if self.name == 'local':
            return 5432
        elif self.name == 'perf-test':
            return 5555
        elif self.name == 'anonymizer-test':
            return 5556
        inst = Repository.get_instance_from_repo_full_name(repo_full_name)
        return self.new_base[self.name] + self.offset[inst]

    def get_old_port(self, repo_full_name=''):
        if self.name == 'sandbox':
            return 5433
        elif self.name == 'dev':
            return 5434
        elif self.name == 'fit':
            return 5435
        elif self.name == 'perf':
            return 5436
        elif self.name == 'train':
            return 5437
        elif self.name == 'test':
            return 5438
        elif self.name == 'cron_test':
            return 5555
        elif self.name == 'local':
            return 5432
        else:
            print(f"utils.get_port('{self.name}')\n" + """"Nem létező környezet:
    Lehetséges értékek:
      sandbox
      dev
      fit
      perf
      train
      test
      new_""")
            raise Exception("Nem létező környezet")

    @staticmethod
    def get_env_name_from_port(port):
        prevkey = ''
        for env, p in Env.new_base.items():
            if int(port) < p:
                return prevkey
            prevkey = env
        return prevkey

    def get_all_databases(self):
        host, port = 'localhost', self.get_port_from_repo()
        cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
        return cluster.databases


    def get_conn_service_user(self, db):
        port = self.get_port_from_repo(Repository.get_repository_name_from_dbname(db))
        try:
            return psycopg2.connect(
                    host='localhost',
                    port=port,
                    database=db,
                    user=utils_db.get_sema_from_dbname(db) + '_service',
                    password='mlffTitkosPassword123!')
        except:
            return None


    def get_conn_from_db_user(self, db, user):
        port = self.get_port_from_repo(Repository.get_repository_name_from_dbname(db))
        p = password_from_file(user, port)
        try:
            return psycopg2.connect(
                host='localhost',
                port=port,
                database=db,
                user=user,
                password=password_from_file(user, port))
        except Exception as e:
            print(e)


def environment_selector() -> Env:
    print('Válassz környezetet!')
    for idx, env in enumerate(Env.new_base):
        print(f'{idx}: {env}')
    idx = int(input('Írd be a sorszámát:'))
    env_name = list(Env.new_base.keys())[idx]
    return Env(env_name)


