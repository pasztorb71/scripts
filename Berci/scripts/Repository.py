import os
import re
from inspect import getfile

import utils
from utils_file import append_to_file_after_line_last_occurence
from Database import Database


class Repository():
    base = 'c:/GIT/MLFF/'

    def __init__(self, name='', schema=''):
        if name:
            self.name = self.find_name(name)
            self.base_path = self.base + self.name + '/liquibase/'
            self.dbname = self.get_db_name()
            self.db_path = self.dbname.replace('-', '_')
            #self.schema = self.get_schema() if not schema else schema
            self.instance = self._get_instance()

    def __str__(self):
        return f'Repository({self.name})'

    @property
    def schema(self):
        return self.get_schema()

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

    @property
    def last_component_ver(self):
        c = self.get_schema_version_label_lines().splitlines()
        if len(c) == 0: return None
        m = re.match('.*labels="(.*), .*', c[-1])
        return m.group(1) if m else None

    @property
    def env_ver(self):
        with open(f'{self.base}{self.name}/.env', 'r', encoding='utf8') as f:
            ver = re.match('.*VERSION=(.*)\n', f.read(), flags=re.DOTALL).group(1)
        return ver.rsplit('.', 1)[0]


    def get_schema(self):
        files = os.listdir(self.base_path + self.db_path)
        noneed = ['install-parameters-db1.xml', 'liquibase-install-db1-step-01.xml', 'liquibase-install-db1-step-02.xml',
                  '_all-modules', '_create_dbs', '__init_dbs', '_init_dbs', 'all-modules', 'partman', 'cron_jobs']
        return list(set(files) - set(noneed))[0]

    @classmethod
    def _get_db_name(cls, base_path):
        name = ''
        m = re.match('.*mlff-(.*)-postgredb', base_path)
        if m:
            name = m.group(1)
        if 'doc-postgredb' in base_path:
            name = 'doc_document'
        return name.replace('-', '_')

    @classmethod
    def get_db_names_by_group(cls, groupname):
        with open(getfile(cls.get_db_names_by_group).rsplit('\\', 1)[0] + '/csapatok.txt', 'r', encoding='utf8') as f:
            lines = f.readlines()
        return [cls._get_db_name(line.split()[0]) for line in lines if groupname in line]

    def get_db_name(self):
        return self._get_db_name(self.base_path)

    def get_schema_version_dir(self):
        return '/'.join([self.base_path[:-1], self.db_path, self.schema, 'tables', '_xml-version-tree'])

    def get_table_version_dir(self):
        return f"{self.get_schema_version_dir()}/version-0"

    def get_tables_dir(self):
        return '/'.join([self.base_path[:-1], self.db_path, self.schema, 'tables'])

    def get_schema_version_label_lines(self):
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


    def modify_schema_version_xml(self, tab_name):
        dirname = self.get_tables_dir()
        ddl_line = f'<include file="{tab_name}/{tab_name}.sql" relativeToChangelogFile="true"/>'
        append_to_file_after_line_last_occurence(f"{dirname}/create-tables.xml", '<include file=', '  ' + ddl_line)
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

    def clear_repo(self, delete_changelog_only=False):
        #if input("Main repo-t kézi eldobása megtörtént? [y/n]") != "y":
        #    return
        if delete_changelog_only:
            self.drop_db_changelog()
        else:
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

    def drop_db_changelog(self):
        clus = Database(self.dbname, 'localhost', '5432')
        clus.sql_exec(f'drop table if exists public.databasechangelog')
        print(f'databasechangelog dropped from {self.dbname} database.')

    def _get_instance(self):
        if self.dbname.startswith('core_'):
            return 'pg-core-mqid'



