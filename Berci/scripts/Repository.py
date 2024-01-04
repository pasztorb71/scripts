import glob
import os
import re
from inspect import getfile

import Database
import Environment
from Cluster import Cluster
from utils import utils_file, utils_sec
from utils.utils_sec import password_from_file


def rel_to_num(release):
    if not release:
        return 999
    if release.count('.') == 2:
        release = release.rsplit('.', 1)[0]
    return float(release[1:])



class Repository():
    base = 'c:/GIT/MLFF/'

    @classmethod
    def get_repo_from_filename(cls, filename):
        return cls(filename.split('\\liquibase')[0].rsplit('\\', 1)[1])


    def __init__(self, name='', schema='', base=base):
        self.base = base
        if name:
            self.name = self.find_name(name)
            self.base_path = self.base + self.name + '/liquibase/'
            self.dbname = self.get_db_name()
            self.db_path = self.dbname.replace('-', '_')
            #self.schema = self.get_schema() if not schema else schema
            self.instance = self._get_instance()
            pass

    def __str__(self):
        return f'Repository({self.name})'

    @staticmethod
    def get_release_label_release_of_file(file):
        file_name = file.rsplit('\\', 1)[1]
        # label = get_label_from_file(file)
        # if label:
        #    return label
        if not os.path.exists(file.rsplit('\\', 2)[0] + '/schema-version-0.xml'):
            return None
        try:
            repo = Repository.get_repo_from_filename(file)
            repo.lines = repo.get_schema_version_0_label_lines()
            label = repo.get_label_of_file_from_schema_version(file_name)
            if label:
                return label
            lines = repo.get_schema_xml_files_labels()
            return repo.get_label_advanced(file, lines)
        except Exception as e:
            print(file)
            raise e

    def get_schema_xml_files_labels(self) -> list[str, str]:
        filelist = []
        for line in self.lines:
            m = re.match(".*(schema-version-.*.xml).*", line)
            if m:
                m_label = re.match('.*labels=.*(R.*)"/>.*', line)
                label = m_label.group(1) if m_label else None
                filelist.append([m.group(1), label])
        return filelist

    def get_label_advanced(self, file, xml_files: list[str, str]):
        sql_file_name = file.rsplit('\\', 1)[1]
        for xml_f in xml_files:
            if not os.path.exists(file.rsplit('\\', 2)[0] + '/schema-version-0.xml'):
                return None
            try:
                lines = []
                schema_version_file = file.rsplit('\\', 2)[0] + f'/{xml_f[0]}'
                with open(schema_version_file, 'r', encoding='utf8') as f:
                    for line in f.readlines():
                        if sql_file_name in line:
                            if xml_f[1]:
                                return xml_f[1]
                            else:
                                m = re.match('.*labels=.*R(.*)"/>.*', line)
                                return m.group(1) if m else None
            except Exception as e:
                print(file)
                raise e

    @staticmethod
    def get_repository_name_from_dbname(db_name):
        repo_names = Repository().get_repo_names()
        for repo in [Repository(x) for x in repo_names]:
            if db_name == repo.get_db_name():
                return repo.name
        return None

    def get_instance_from_repo_full_name(repo):
        if repo == 'doc-postgredb':
            return 'pg-doc'
        else:
            id = repo.split('-')[1]
            return 'pg-' + id

    @staticmethod
    def get_repos_containing_release(rname):
        out = []
        for repo in Repository().get_repo_names():
            if utils_file.file_contains(f'{Repository(repo).get_tables_dir()}/schema-version-0.xml', rname):
                out.append(repo)
        return out

    @staticmethod
    def get_repos_from_port(port):
        cluster = Cluster(host='localhost', port=port, passw=password_from_file('postgres', 'localhost', port))
        dbs = cluster.databases
        return Database.get_repositories_from_dbs(dbs)

    @staticmethod
    def get_all_repos_by_group(group):
        return [Repository.Repository(x) for x in Repository.Repository.get_repo_names_by_group(group)]

    @property
    def schema(self):
        return self.get_schema()

    def get_name(self):
        return self.name

    def get_base(self):
        return self.__class__.base

    def get_base_path(self):
        return self.base_path

    def find_name(self, name):
        repos = os.listdir(self.base)
        a = [repo for repo in repos if name in repo]
        if len(a) > 1:
            print("Nem egyértelmű a repository név!")
            print("Melyiket választod?")
            for idx, value in enumerate(a):
                print(f'{idx}: {value}')
            i = int(input())
            a = [a[i]]
        return a[0]

    @staticmethod
    def get_repo_names():
        return os.listdir(__class__.base)

    @staticmethod
    def get_repo_names_exclude(excludelist):
        return [name for name in os.listdir(__class__.base) if not any (x in name for x in excludelist)]

    @classmethod
    def get_repo_names_by_group(cls, groupname):
        with open(getfile(cls.get_db_names_by_group).rsplit('\\', 1)[0] + '/csapatok.txt', 'r', encoding='utf8') as f:
            lines = f.readlines()
        return [line.split()[0] for line in lines if groupname in line]

    def last_component_ver(self, max_release: str = None) -> list[str, str]:
        lines = self.get_schema_version_0_label_lines()
        if len(lines) == 0: return None
        out = []
        for line in reversed(lines):
            m = re.match('.*labels="(.*), (.*)".*', line)
            if m:
                if rel_to_num(max_release) >= rel_to_num(m.group(2)):
                    out = [m.group(1).replace('.0', '.'), m.group(2)]
                    break
            else:
                out = [None, None]
        return out

    @property
    def env_ver(self):
        with open(f'{self.base}{self.name}/.env', 'r', encoding='utf8') as f:
            ver = re.match('.*VERSION=(.*)\n', f.read(), flags=re.DOTALL).group(1)
        return ver.rsplit('.', 1)[0]


    def get_schema(self):
        files = os.listdir(self.base_path + self.db_path)
        noneed = ['install-parameters-db1.xml', 'liquibase-install-db1-step-01.xml', 'liquibase-install-db1-step-02.xml',
                  'liquibase-install-db-step-01.xml', 'liquibase-install-schema-step-02.xml', 'install-parameters.xml',
                  '_all-modules', '_create_dbs', '__init_dbs', 'init_dbs', '_init_dbs', 'all-modules', 'partman', 'cron_jobs',
                  'create_publication.sql', 'ddl_changes_module', 'create_extensions.sql']
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

    def get_schema_version_0_label_lines(self) -> list[str]:
        with open(f'{self.get_tables_dir()}/schema-version-0.xml', 'r', encoding='utf8') as f:
            lines = [line for line in f.read().split('\n') #if 'labels=' in line
                     ]
            """
            if len(lines) > 10:
                lines = lines[-10:]
            """
            return lines

    def get_label_of_file_from_schema_version(self, file):
        for line in self.lines:
            if file in line:
                m = re.match('.*labels=.*R(.*)"/>.*', line)
                return m.group(1) if m else None
        return None

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
        utils_file.append_to_file_after_line_last_occurence(f"{dirname}/create-tables.xml", '<include file=', '  ' + ddl_line)
        print('Line added to create-tables.xml')
        print(ddl_line)


    def get_tablename_from_indexname(self, indexname):
        arr = indexname.split('.')
        schema, iname = arr[0], arr[1]
        conn = Environment.Env('local').get_conn_from_db_user(self.dbname, 'postgres')
        cur = conn.cursor()
        cur.execute(f"SELECT tablename FROM pg_catalog.pg_indexes where schemaname = '{schema}' and indexname = '{iname}'")
        tabname = cur.fetchone()[0]
        conn.close()
        return tabname

    def clear_repo(self, delete_changelog_only=False, confirm=True):
        #if input("Main repo-t kézi eldobása megtörtént? [y/n]") != "y":
        #    return
        if delete_changelog_only:
            self.drop_db_changelog()
        else:
            self.drop_database()
            self.drop_roles()
            self.drop_main_changelog()
        if confirm == False:
            return True
        if input("Mehet a telepítés? [y/n]") == "y":
            return True


    def drop_database(self):
        clus = Database.Database('postgres', '5432')
        clus.sql_exec(f'drop database if exists {self.dbname}')
        print(f'{self.dbname} database dropped.')

    def drop_roles(self):
        clus = Database.Database('postgres', '5432')
        clus.drop_roles(self.schema)

    def drop_main_changelog(self):
        clus = Database.Database('postgres', '5432')
        clus.sql_exec(f'drop table if exists public.databasechangelog')
        print(f'public.databasechangelog dropped.')

    def drop_db_changelog(self):
        clus = Database.Database(self.dbname, '5432')
        clus.sql_exec(f'drop table if exists public.databasechangelog')
        print(f'databasechangelog dropped from {self.dbname} database.')

    def _get_instance(self):
        if self.dbname.startswith('core_'):
            return 'pg-core-mqid'

    def is_new_type_sql_numbering(self):
        return len(glob.glob(f'{self.get_tables_dir()}/*.xml')) > 1

    @property
    def image_name_with_release(self):
        with open(f'{self.base + self.name}/.env') as envfile:
            lines = envfile.read().split()
        return lines[0].split('=')[1] + lines[1].split('}')[1] + ':' + lines[2].split('=')[1]

    @property
    def image_run_command(self):
        name = self.image_name_with_release
        password = utils_sec.password_from_file('postgres', Environment.Env('local').get_port_from_repo(self.name))
        return ('docker run --rm --network mlff-local-network -e DB_ADDRESS=gateway.docker.internal '
                       f'-e DB_PORT=5432 -e POSTGRES_PASSWORD={password} {name}')

    @property
    def image_build_command(self):
        base_name = self.base.replace('/', '\\') + self.name
        return f"docker-compose --env-file {base_name}\\.env -f {base_name}\etc\\release\\docker-compose.yml build"

    @property
    def run_sh_eol_type(self):
        with open(self.base + self.name + '/run.sh') as f:
            oneline = f.readline()
        if f.newlines == '\r\n':
            return 'windows'
        return 'unix'

def get_all_repos() -> list[Repository]:
    return [Repository(x) for x in Repository.get_repo_names()]


