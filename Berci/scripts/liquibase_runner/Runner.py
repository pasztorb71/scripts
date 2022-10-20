import glob
import os

import utils
from Repository import Repository
from docker_ips import ipdict, base_ips
from utils import get_dbname_from_project


class Runner:
    repos = []
    def __init__(self, base, repos=[]):
        self.base = base
        self.password = ''
        self.loc = ''
        self.delete_db_before = False
        Runner.repos = repos

    def _call_liquibase(self, project, env, postgrespass, db):
        print(project + ' : ' + db)
        cmd = '''docker run --rm -v #base##project#\liquibase\:/liquibase/changelog liquibase/liquibase:4.15 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/#db# --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=#changelog# update'''
        if self.checkonly:
            cmd = cmd.replace('update', 'status --verbose')
        cmd = cmd\
            .replace('#base#', self.base)\
            .replace('#project#', project)\
            .replace('#env#', env)\
            .replace('#password#', postgrespass)\
            .replace('#db#', db)\
            .replace('#projectdb#', get_dbname_from_project(project))\
            .replace('#changelog#', self.get_changelog(db, project))
        #ret_code = os_command(cmd)
        #print(cmd)
        #return
        #self.confirm('')
        ret_code = os.system(cmd)
        if ret_code != 0:
            exit(ret_code)

    def get_changelog(self, db, project):
        db_name = get_dbname_from_project(project)
        return  db_name+'\liquibase-install-db1-step-01.xml' if db == 'postgres' else db_name+'\liquibase-install-db1-step-02.xml'

    def get_dbs(self, repo):
            if repo == 'doc-postgredb':
                return ['document']
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

    def get_ip_addresses_for_docker(self, loc):
        if loc in ['remote', 'all']:
            return ipdict[loc]
        else:
            return base_ips[loc]

    def run_for_repo(self, ip_address, repo):
        if self.delete_db_before:
            if self.loc != 'local':
                exit('Nem local esetén nem dobható el az adatbázis!!!')
            Repository(repo).clear_repo()
        self._call_liquibase(repo, ip_address, self.password, 'postgres')
        for db in self.get_dbs(repo):
            self._call_liquibase(repo, ip_address, self.password, db)

    def run(self, loc, delete_db_before, checkonly):
        if not checkonly and not self.confirm(loc): return
        self.delete_db_before = delete_db_before
        self.loc = loc
        self.checkonly = checkonly
        self.password = 'fLXyFS0RpmIX9uxGII4N' if loc != 'local' else 'mysecretpassword'
        for ip_address in self.get_ip_addresses_for_docker(loc):
            print(ip_address)
            for repo in [repo.get_name() for repo in self.repos]:
                self.run_for_repo(ip_address, repo)

    def kill(self, param):
        pass

    def run_additional_script(self):
        pass

    @classmethod
    def confirm(cls, loc):
        print(f"Az alábbi repokra lesz telepítve, host: {loc}")
        for r in Runner.repos:
            print(f" - {r.get_name()}")
        if input("Mehet a telepítés? [y/n]") == "y":
            return True


