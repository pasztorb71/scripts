import glob
import os

from utils import get_dbname_from_project


class Runner:
    def __init__(self, base, repos=[]):
        self.base = base
        self.password = ''
        self.loc = ''
        self.full = False
        self.repos = repos

    def _call_liquibase(self, project, env, postgrespass, db):
        print(project + ' : ' + db)
        cmd = '''docker run --rm -v #base##project#\liquibase\#projectdb#\:/liquibase/changelog liquibase/liquibase:4.12 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/#db# --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=#changelog# update'''
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

    def get_ip_addresses(self, loc):
        if loc == 'remote':
            return ['gateway.docker.internal:5433',
                    'gateway.docker.internal:5434']
        elif loc == 'all':
                return ['gateway.docker.internal:5433',
                        'gateway.docker.internal:5434',
                        'gateway.docker.internal:5435',
                        ]
        elif loc == 'local':
            return ['gateway.docker.internal']
        elif loc == 'sandbox':
            return ['gateway.docker.internal:5433']
        elif loc == 'dev':
            return ['gateway.docker.internal:5434']
        elif loc == 'fit':
            return ['gateway.docker.internal:5435']
        elif loc == 'perf':
            return ['gateway.docker.internal:5436']

    def run_for_repo(self, ip_address, repo):
        if self.full:
            self.clear_repo()
        self._call_liquibase(repo, ip_address, self.password, 'postgres')
        for db in self.get_dbs(repo):
            self._call_liquibase(repo, ip_address, self.password, db)

    def run(self, loc, full, checkonly):
        self.full = full
        self.loc = loc
        self.checkonly = checkonly
        self.password = 'fLXyFS0RpmIX9uxGII4N' if loc != 'local' else 'mysecretpassword'
        for ip_address in self.get_ip_addresses(loc):
            print(ip_address)
            for repo in [repo.get_name() for repo in self.repos]:
                self.run_for_repo(ip_address, repo)

    def kill(self, param):
        pass

    def run_additional_script(self):
        pass

    def clear_repo(self):
        pass


