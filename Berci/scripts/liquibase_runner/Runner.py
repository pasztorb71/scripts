import glob
import logging
import os

import Environment
from utils import utils_sec
from Repository import Repository
from utils.utils import get_ip_address_for_docker
from utils.utils_db import get_dbname_from_project


class Runner:
    repos = []
    def __init__(self, repos=[], confirm=True):
        self.base = 'c:/GIT/MLFF/'
        self.password = ''
        self.loc = ''
        self.delete_db_before = False
        self.confirm_one_run = confirm
        Runner.repos = repos
        logging.basicConfig(level=logging.DEBUG, filename='liquibase_run.log', filemode='a', format='%(asctime)s - %(message)s')

    def _call_liquibase(self, project, env, postgrespass, db):
        print(project + ' : ' + db)
        cmd = '''docker run --rm -v #base##project#\liquibase\:/liquibase/changelog liquibase/liquibase:4.21 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/#db# --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=#changelog# #context# update'''
        if self.checkonly:
            cmd = cmd.replace('update', 'status --verbose')
        cmd = cmd\
            .replace('#base#', self.base)\
            .replace('#project#', project)\
            .replace('#env#', env)\
            .replace('#password#', postgrespass)\
            .replace('#db#', db)\
            .replace('#projectdb#', get_dbname_from_project(project))\
            .replace('#changelog#', self.get_changelog(db, project))\
            .replace('#context#', self.get_context())
        #ret_code = os_command(cmd)
        #print(cmd)
        #return
        #self.confirm('')
        ret_code = os.system(cmd)
        if ret_code != 0:
            exit(ret_code)

    def get_changelog(self, db, project):
        db_name = get_dbname_from_project(project)
        if db_name in ['enforcement_onsite_inspection']:
            return  db_name+'\liquibase-install-db-step-01.xml' if db == 'postgres' else db_name+'\liquibase-install-schema-step-02.xml'
        else:
            return db_name + '\liquibase-install-db1-step-01.xml' if db == 'postgres' else db_name + '\liquibase-install-db1-step-02.xml'

    def get_context(self):
        return '--contexts=sand' if self.loc=='sandbox' else ''

    def get_dbs(self, repo):
            if repo == 'doc-postgredb':
                return ['doc_document']
            t = repo.split('-')
            return ['_'.join(t[1:-1])]

    def get_dbs_old(self, repo):
            if repo == 'mlff-core-customer-postgredb':
                return ['core_customer']
            elif repo == 'mlff-enforcement-exemption-postgredb':
                return ['enforcement_exemption']
            path = self.base + repo + '/liquibase/*.xml'
            files = glob.glob(path)
            files = [f.split('\\')[1] for f in files if 'liquibase-install-databases.xml' not in f]
            dblist = [file.replace('liquibase-install-','').replace('.xml','') for file in files]
            return dblist

    def run_for_repo(self, ip_address, repo, delete_changelog_only=False):
        print(f"Környezet IP: {ip_address}")
        print(f"Az alábbi repora lesz telepítve: {repo}")
        if not self.checkonly:
            try:
                print(Repository(repo).get_schema_version_label_lines())
            except FileNotFoundError:
                pass
        if self.confirm_one_run == True:
            if input("Mehet a telepítés? [y/n]") != "y":
                print('Telepítés megszakítva!')
                return
        logging.info(f"{repo} - {self.loc} - Delete_before:{self.delete_db_before} - Checkonly:{self.checkonly}")
        if self.delete_db_before:
            if self.loc != 'local':
                exit('Nem local esetén nem dobható el az adatbázis!!!')
            if not Repository(repo).clear_repo(delete_changelog_only, self.confirm_one_run):
                return
        self._call_liquibase(repo, ip_address, self.password, 'postgres')
        for db in self.get_dbs(repo):
            self._call_liquibase(repo, ip_address, self.password, db)

    def run_multiple_repos(self, loc, checkonly, delete_db_before=False, delete_changelog_only=False):
        if not checkonly:
            if not self.confirm(loc): return
        else:
            self.confirm_one_run = False
        self.delete_db_before = delete_db_before
        self.loc = loc
        self.checkonly = checkonly
        for repo in [repo.get_name() for repo in self.repos]:
            self.password = utils_sec.password_from_file('postgres', Environment.Env(loc).get_port_from_repo(repo))
            self.run_for_repo(get_ip_address_for_docker(repo, loc), repo, delete_changelog_only)

    def kill(self, param):
        pass

    def run_additional_script(self):
        pass

    @classmethod
    def confirm(cls, loc):
        if len(Runner.repos) == 1:
            return True
        print(f"Az alábbi repokra lesz telepítve, host: {loc}")
        for r in Runner.repos:
            print(f" - {r.get_name()}")
        if input("Mehet a telepítés? [y/n]") == "y":
            return True


