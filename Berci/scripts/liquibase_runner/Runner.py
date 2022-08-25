import glob
import os

from docker_ips import ipdict, base_ips
from utils import get_dbname_from_project


class Runner:
    repos = []
    def __init__(self, base, repos=[]):
        self.base = base
        self.password = ''
        self.loc = ''
        self.full = False
        Runner.repos = repos

    def _call_liquibase(self, project, env, postgrespass, db):
        print(project + ' : ' + db)
        cmd = '''docker run --rm -v #base##project#\liquibase\#projectdb#\:/liquibase/changelog liquibase/liquibase:4.7 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/#db# --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=#changelog# update'''
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
        ret_code = os.system(cmd)
        if ret_code != 0:
            exit(ret_code)

    def get_changelog_old(self, db, project):
        if project == 'mlff-core-customer-postgredb':
            return 'core_customer\liquibase-install-step-01.xml' if db == 'postgres' else 'core_customer\liquibase-install-step-02.xml'
        elif project == 'mlff-enforcement-exemption-postgredb':
            return 'enforcement_exemption\liquibase-install-step-01.xml' if db == 'postgres' else 'enforcement_exemption\liquibase-install-step-02.xml'
        return 'liquibase-install-databases.xml' if db == 'postgres' else 'liquibase-install-' + db + '.xml'

    def get_changelog(self, db, project):
        if os.path.isfile(self.base+project+'/liquibase/liquibase-install-databases.xml'):
            return 'liquibase-install-databases.xml' if db == 'postgres' else 'liquibase-install-' + db + '.xml'
        return 'liquibase-install-step-01.xml' if db == 'postgres' else 'liquibase-install-step-02.xml'

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
        if self.full:
            self.clear_repo()
        self._call_liquibase(repo, ip_address, self.password, 'postgres')
        for db in self.get_dbs(repo):
            self._call_liquibase(repo, ip_address, self.password, db)

    def run(self, loc, full, checkonly):
        if not checkonly and not self.confirm(loc): return
        self.full = full
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

    def clear_repo(self):
        pass

    @classmethod
    def confirm(cls, loc):
        print(f"Az alábbi repokra lesz telepítve, host: {loc}")
        for r in Runner.repos:
            print(f" - {r.get_name()}")
        if input("Mehet a telepítés? [y/n]") == "y":
            return True


