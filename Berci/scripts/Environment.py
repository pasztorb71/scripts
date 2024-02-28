from __future__ import annotations

import logging
from dataclasses import dataclass, asdict, field

import psycopg2
import yaml

import Repository
from sql_runner.parallel_runner.thread import Querydata, dbcommand_thread_executor
from utils import utils_db
from Cluster import Cluster
import Database
from utils.utils_sec import password_from_file

PORT_DATABASES_FROM_ENVS = 'c:/Users/bertalan.pasztor/PycharmProjects/liquibase/Berci/scripts/backup/port_databases_from_envs.yaml'

@dataclass
class Domain:
    name: str = field(repr=True)
    port: int = field(repr=False)
    databases: list[str] = field(repr=False)

@dataclass
class Env_db:
    env_name: str
    domains: list[Domain]

class Env:
    _domain_databases = {
        'doc':
            'doc_document',
        'core':
            'core_analytic,core_customer,core_genos,core_notification_dispatcher,core_notification_email,'
            'core_notification_wa,core_privateuser,core_ticket,core_vehicledoc_document',
        'enforcement':
            'enforcement_detection,enforcement_detection_alert,enforcement_detection_image,enforcement_detection_observation,'
            'enforcement_detection_transit_identifier,enforcement_detection_transition,enforcement_eligibility,'
            'enforcement_exemption,enforcement_onsite_alert,enforcement_onsite_alert_subscribe,enforcement_onsite_inspection,'
            'enforcement_sanctioning_presumption,enforcement_sanctioning_sanction,enforcement_visual_check',
        'eobu':
            'eobu_tariff,eobu_trip',
        'notification':
            'core_notification_dispatcher,core_notification_email, core_notification_wa',
        'payment':
            'payment_account_info,payment_invoice,payment_psp_proxy,payment_transaction',
        'settlement':
            'settlement_psp_clearing,settlement_tro_clearing',
        'obu':
            'obu_obuprovider'
    }
    test = {'mlff_test': 5555}
    _env_ports = {'local': 5432,
                'sandbox': 5440,
                'dev': 5540,
                'fit': 5640,
                'cantas_train': 5740,
                'cantas_test': 5840,
                'perf': 5940,
                'cantas_dev': 6040,
                'cantas_prod': 6140,
                'tollgo': 7140
                  }
    _domain_offsets = {'doc': 0,
              'core': 1,
              'enforcement': 2,
              'eobu': 3,
              'payment': 4,
              'settlement': 5,
              'obu': 7,
              'notification': 8,
                       }

    _domains = {'pg-doc': 0,
              'pg-core': 1,
              'pg-enforcement': 2,
              'pg-eobu': 3,
              'pg-payment': 4,
              'pg-settlement': 5,
              'pg-obu': 7,
              'pg-notification': 8,
                }
    list_of_envs = []

    @classmethod
    def get_domain_from_dbname(cls, dbname):
        for domain, dbs in cls._domain_databases.items():
            if dbname in dbs:
                return domain
        return None

    @classmethod
    def build_list_of_envs_from_databases(cls):
        domains = []
        for domain in list(Env._domain_databases)[0:]:
            d = Domain(domain, None, Env._domain_databases[domain].split(','))
            domains.append(d)
        for env_name, port in Env._env_ports.items():
            if env_name == 'local':
                all_databases = ','.join(list(Env._domain_databases.values()))
                d = Domain('local', 5432, all_databases)
                e = Env_db(env_name, [d])
            else:
                e = Env_db(env_name, domains.copy())
                for d in e.domains:
                    d.port = Env._domain_offsets[d.name] + port
            Env.list_of_envs.append(asdict(e))

    @classmethod
    def environment_selector(cls) -> Env:
        print('Válassz környezetet!')
        for idx, env in enumerate(Env._env_ports):
            print(f'{idx}: {env}')
        idx = int(input('Írd be a sorszámát:'))
        env_name = list(Env._env_ports.keys())[idx]
        return Env(env_name)

    @staticmethod
    def get_envs(exclude=['']) -> list[str]:
        (Env._env_ports).update(Env.test)
        return [env for env in Env._env_ports if env not in exclude]

    @staticmethod
    def is_valid_location(name):
        (Env._env_ports).update(Env.test)
        valid = name in Env._env_ports
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
        for port in self.get_ports():
            db = Database.Database('postgres', str(port))
            rows = db.sql_query("SELECT datname from pg_database WHERE datistemplate IS FALSE "
                                "AND datname NOT IN ('cloudsqladmin', 'postgres')")
            names += [x[0] for x in rows]
        return names

    @property
    def databases(self):
        dblist = []
        logging.debug(f'Portok: {self.get_ports()}')
        sql = "SELECT datname from pg_database WHERE datistemplate IS FALSE " \
              "AND datname NOT IN ('cloudsqladmin', 'postgres')"
        res_dict = {}
        qd_list = []
        for port in self.get_ports():
            qd_list.append(Querydata(port, 'postgres', sql, res_dict))
        result = dbcommand_thread_executor(qd_list)
        for db_port in result.keys():
            port = db_port.split('__')[0]
            dblist += [Database.Database(x[0],port) for x in result[db_port]]
        return dblist

    def get_port_from_inst(self, inst):
        if self.name in self.test:
            return self.test[self.name]
        if self.name in self._env_ports:
            if inst in self._domains:
                return self._env_ports[self.name] + self._domains[inst]
            else:
                print("Lehetséges instance-ok:")
                print('\n'.join([x for x in self._domains.keys()]))
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
        for idx in self._domains.values():
            ports.append(self._env_ports[self.name] + idx)
        return ports

    def get_port_from_repo(self, repo_full_name: str) -> int:
        if self.name == 'local':
            return 5432
        elif self.name == 'mlff_test':
            return 5555
        elif self.name == 'anonymizer-test':
            return 5556
        inst = Repository.Repository.get_instance_from_repo_full_name(repo_full_name)
        return self._env_ports[self.name] + self._domains[inst]

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
        for env, p in Env._env_ports.items():
            if int(port) - p < 100:
                return env
        return None

    def get_all_databases(self):
        host, port = 'localhost', self.get_port_from_repo()
        cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
        return cluster.databases


    def get_conn_service_user(self, db):
        port = self.get_port_from_repo(Repository.Repository.get_repository_name_from_dbname(db))
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
        port = self.get_port_from_repo(Repository.Repository.get_repository_name_from_dbname(db))
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


def ports_databases_from_backup():
    with open(PORT_DATABASES_FROM_ENVS, 'r') as b:
        port_databases = yaml.load(b, Loader=yaml.Loader)
    return port_databases

if __name__ == '__main__':


    Env.build_list_of_envs_from_databases()

    with open(PORT_DATABASES_FROM_ENVS, 'w') as b:
        yaml.dump(envs, b, sort_keys=False)


