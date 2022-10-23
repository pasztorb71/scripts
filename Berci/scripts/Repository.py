import os
import re

import psycopg2

import utils
from Database import Database
from utils import get_port


class Repository():
    base = 'c:\\GIT\\MLFF\\'

    def __init__(self, name='', schema=''):
        if name:
            self.name = self.find_name(name)
            self.base_path = 'c:/GIT/MLFF/' + self.name + '/liquibase/'
            self.dbname = self.get_db_name()
            self.db_path = self.dbname.replace('-', '_')
            self.schema = self.get_schema() if not schema else schema

    def __str__(self):
        return f'Repository({self.name})'

    def show(self):
        print("""  A.  mlff-core-customer-postgredb                         JAKARTA   telepítése
  B.  mlff-core-notification-dispatcher-postgredb          KOMODO    telepítése
  C.  mlff-core-notification-email-postgredb               KOMODO    telepítése
  D.  mlff-core-notification-pn-postgredb                  KOMODO    telepítése
  E.  mlff-core-notification-wa-postgredb                  KOMODO    telepítése
  F.  mlff-core-template-postgredb                         KOMODO    telepítése
  G.  mlff-core-ticket-postgredb                           KOMODO    telepítése
  H.  mlff-core-vehicle-postgredb                          KOMODO    telepítése

  I.  mlff-enforcement-detection-image-postgredb           N2O       telepítése
  J.  mlff-enforcement-detection-postgredb                 N2O       telepítése
  K.  mlff-enforcement-visual-check-postgredb              N2O       telepítése
  K.  mlff-enforcement-detection-observation-postgredb     N2O       telepítése

  L.  mlff-enforcement-exemption-postgredb                 JAKARTA   telepítése
  M.  mlff-eobu-tariff-postgredb                           JAKARTA   telepítése
  N.  mlff-eobu-trip-postgredb                             JAKARTA   telepítése
  O.  mlff-data-ingestion-meta-postgredb                   DWH       telepítése
  P.  mlff-payment-account-info-postgredb                  LIBRA     telepítése
  Q.  mlff-payment-psp-proxy-postgredb                     LIBRA     telepítése
  R.  mlff-payment-retry-postgredb                         LIBRA     telepítése
  S.  mlff-payment-transaction-postgredb                   LIBRA     telepítése
  T.  mlff-settlement-tro-clearing-postgredb               LIBRA     telepítése
  T.  mlff-settlement-tro-clearing-postgredb               LIBRA     telepítése
  U.  mlff-payment-invoice-postgredb                       LIBRA     telepítése

  V.  mlff-enforcement-eligibility-declaration-postgredb   K-Team    telepítése
  W.  mlff-enforcement-eligibility-detection-postgredb     K-Team    telepítése

  Y.  doc-postgredb                  modul telepítése      iCell belsős""")

    def get_name(self):
        return self.name

    def get_base(self):
        return self.__class__.base

    def get_base_path(self):
        return self.base_path

    @staticmethod
    def find_name(name):
        repos = os.listdir(__class__.base)
        a = [repo for repo in repos if name in repo]
        if len(a) > 1:
            print(a)
            raise Exception("Nem egyértelmű a repository név!")
        return a[0]

    def get_repo_names(self):
        return os.listdir(self.__class__.base)


    def get_schema(self):
        line = ''
        pattern = '.*property name="schema_name.*value="(.*)"/>'
        p = self.base_path+self.db_path+'/' + self.get_sema_from_dbname(self.db_path)
        with open(self.get_base_path()+self.db_path+'/' + self.get_sema_from_dbname(self.db_path) + '/liquibase-install-schema.xml', 'r', encoding='utf-8') as f:
            text = f.read().splitlines()
            for l in text:
                m = re.match(pattern, l)
                if m:
                    return m.group(1)
        return ''

    def get_db_name(self):
        name = ''
        m = re.match('.*mlff-(.*)-postgredb', self.base_path)
        if m:
            name = m.group(1)
        if 'doc-postgredb' in self.base_path:
            name = 'document'
        return name.replace('-', '_')

    def get_schema_version_dir(self):
        return '/'.join([self.base_path[:-1], self.db_path, self.schema, 'tables', '_xml-version-tree'])

    def get_table_version_dir(self):
        return f"{self.get_schema_version_dir()}/version-0"

    def get_tables_dir(self):
        return '/'.join([self.base_path[:-1], self.db_path, self.schema, 'tables'])

    @staticmethod
    def get_sema_from_dbname(db):
        if db == 'document':
            return 'document_meta'
        if db == 'payment_transaction':
            return 'payment_transaction'
        return db.split('_', 1)[1]

    def is_table_file_exists(self, tablename):
        dirname = self.get_tables_dir()
        if not os.path.isdir(f"{dirname}/{tablename}"):
            return False
        if os.path.isfile(f"{dirname}/{tablename}/{tablename}-DDL-000.sql"):
            return True
        return False

    def create_tablefile(self, tab_name):
        dirname = self.get_tables_dir()
        if not os.path.isdir(f"{dirname}/{tab_name}"):
            os.mkdir(f"{dirname}/{tab_name}")
        fname = f"{dirname}/{tab_name}/{tab_name}-DDL-000.sql"
        open(fname, 'a').close()
        print(f"{fname} file created.")


    def schema_version_xml(self, tab_name):
        dirname = self.get_tables_dir()
        ddl_line = f'<include file="{tab_name}/{tab_name}.sql" relativeToChangelogFile="true"/>'
        utils.append_to_file_after_line_last_occurence(f"{dirname}/create-tables.xml", '<include file=', '  ' + ddl_line)
        print('Line added to create-tables.xml')
        print(ddl_line)


    def get_tablename_from_indexname(self, indexname):
        arr = indexname.split('.')
        schema, iname = arr[0], arr[1]
        conn = utils.get_conn('local', self.dbname, 'postgres')
        cur = conn.cursor()
        cur.execute(f"SELECT tablename FROM pg_catalog.pg_indexes where schemaname = '{schema}' and indexname = '{iname}'")
        tabname = cur.fetchone()[0]
        conn.close()
        return tabname

    def clear_repo(self):
        #if input("Main repo-t kézi eldobása megtörtént? [y/n]") != "y":
        #    return
        self.drop_database()
        self.drop_roles()
        self.drop_main_changelog()
        if input("Mehet a telepítés? [y/n]") == "y":
            return True


    def drop_database(self):
        clus = Database('postgres', 'localhost', '5432')
        clus.sql_exec(f'drop database if exists {self.dbname}')
        print(f'{self.dbname} database dropped.')

    def drop_roles(self):
        clus = Database('postgres', 'localhost', '5432')
        clus.drop_roles(self.schema)

    def drop_main_changelog(self):
        clus = Database('postgres', 'localhost', '5432')
        clus.sql_exec(f'drop table if exists public.databasechangelog')
        print(f'public.databasechangelog dropped.')



def get_conn_service_user(env, db):
    port = get_port(env)
    try:
        return psycopg2.connect(
            host='localhost',
            port=port,
            database=db,
            user=Repository.get_sema_from_dbname(db) + '_service',
            password='mlffTitkosPassword123!')
    except:
        return None