import os
import re

import utils
from Database import Database
from utils import get_sema_from_dbname


class Repository():
    base = 'c:\\GIT\\MLFF\\'

    def __init__(self, name='', schema=''):
        if name:
            self.name = self.find_name(name)
            self.base_path = 'c:/GIT/MLFF/' + self.name + '/liquibase/'
            self.dbname = self.get_db_name()
            self.db_path = self.dbname.replace('-', '_')
            self.schema = self.get_schema() if not schema else schema
            self.instance = self._get_instance()

    def __str__(self):
        return f'Repository({self.name})'

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
        p = self.base_path + self.db_path +'/' + get_sema_from_dbname(self.db_path)
        with open(self.get_base_path() + self.db_path +'/' + get_sema_from_dbname(self.db_path) + '/liquibase-install-schema.xml', 'r', encoding='utf-8') as f:
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

    def get_schema_version_content(self):
        with open(f'{self.get_tables_dir()}/schema-version-0.xml', 'r', encoding='utf8') as f:
            return ''.join([line for line in f.readlines() if 'labels=' in line])

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

    def _get_instance(self):
        if self.dbname.startswith('core_'):
            return 'pg-core-mqid'



