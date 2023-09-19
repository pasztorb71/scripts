import psycopg2

import Repository
from utils import utils_db
from Cluster import Cluster
import Database
from utils.utils_sec import password_from_file


class Env():
    test = {'mlff_test': 5555}
    base = {'local': 5432,
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

    @staticmethod
    def is_valid_location(name):
        (Env.base).update(Env.test)
        valid = name in Env.base
        if not valid:
            print(f"Not valid location: {name}")
            print("Possible locations:")
            print('  ' + '\n  '.join(get_envs()))
        return valid

    def __init__(self, name='local'):
        if name:
            if not Env.is_valid_location(name):
                exit(1)
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
        if self.name in self.test:
            return self.test[self.name]
        if self.name in self.base:
            if inst in self.offset:
                return self.base[self.name] + self.offset[inst]
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
            ports.append(self.base[self.name] + idx)
        return ports

    def get_port_from_repo(self, repo_full_name: str) -> int:
        if self.name == 'local':
            return 5432
        elif self.name == 'mlff_test':
            return 5555
        elif self.name == 'anonymizer-test':
            return 5556
        inst = Repository.get_instance_from_repo_full_name(repo_full_name)
        return self.base[self.name] + self.offset[inst]

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
        for env, p in Env.base.items():
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
    for idx, env in enumerate(Env.base):
        print(f'{idx}: {env}')
    idx = int(input('Írd be a sorszámát:'))
    env_name = list(Env.base.keys())[idx]
    return Env(env_name)


def get_envs(exclude=['']) -> list[str]:
    (Env.base).update(Env.test)
    return [env for env in Env.base if env not in exclude]