import os
import re

class Repository():
    base = 'c:/GIT/MLFF/'

    def __init__(self, name=''):
        if name:
            self.name = self.find_name(name)
            self.base_path = 'c:/GIT/MLFF/' + self.name + '/liquibase/'
            self.dbname = self.get_db_name()
            self.db_path = self.dbname.replace('-', '_')
            self.schema = self.get_schema()

    def get_name(self):
        return self.name

    def get_base(self):
        return self.__class__.base

    def get_base_path(self):
        return self.base_path

    def find_name(self, name):
        repos = os.listdir(self.__class__.base)
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
        return '/'.join([self.base_path[:-1], self.db_path, self.schema, 'xml-version-tree'])

    def get_tables_dir(self):
        return '/'.join([self.base_path[:-1], self.db_path, self.schema, 'tables'])

    def get_sema_from_dbname(self, db):
        if db == 'document':
            return 'document_meta'
        if db == 'payment_transaction':
            return 'payment_transaction'
        return db.split('_', 1)[1]