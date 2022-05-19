import glob
import os


class Runner:
    def __init__(self, base):
        self.base = base
        self.password = ''

    def _call_liquibase(self, project, env, postgrespass, db):
        print(project + ' : ' + db)
        cmd = '''docker run --rm -v #base##project#\liquibase\:/liquibase/changelog liquibase/liquibase:latest --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/#db# --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=#changelog# update'''
        cmd = cmd\
            .replace('#base#', self.base)\
            .replace('#project#', project)\
            .replace('#env#', env)\
            .replace('#password#', postgrespass)\
            .replace('#db#', db)\
            .replace('#changelog#', self.get_changelog(db, project))
        #print(cmd)
        ret_code = os.system(cmd)
        if ret_code != 0:
            exit(ret_code)

    def get_changelog(self, db, project):
        if project == 'mlff-core-customer-postgredb':
            return 'core_customer\liquibase-install-step-01.xml' if db == 'postgres' else 'core_customer\liquibase-install-step-02.xml'
        return 'liquibase-install-databases.xml' if db == 'postgres' else 'liquibase-install-' + db + '.xml'

    def get_dbs(self, repo):
            if repo == 'mlff-core-customer-postgredb':
                return ['core_customer']
            path = self.base + repo + '/liquibase/*.xml'
            files = glob.glob(path)
            files = [f.split('\\')[1] for f in files if 'liquibase-install-databases.xml' not in f]
            dblist = [file.replace('liquibase-install-','').replace('.xml','') for file in files]
            return dblist

    def get_ip_addresses(self, loc):
        if loc == 'remote':
            return ['gateway.docker.internal:5433','gateway.docker.internal:5434']
        elif loc == 'local':
            return ['gateway.docker.internal']
        elif loc == 'sandbox':
            return ['gateway.docker.internal:5433']
        else: #DEV
            return ['gateway.docker.internal:5434']

    def run_for_repo(self, ip_address, repo):
        self._call_liquibase(repo, ip_address, self.password, 'postgres')
        for db in self.get_dbs(repo):
            self._call_liquibase(repo, ip_address, self.password, db)

    def run(self, repos, loc):
        self.password = 'fLXyFS0RpmIX9uxGII4N' if loc == 'remote' else 'mysecretpassword'
        for ip_address in self.get_ip_addresses(loc):
            print(ip_address)
            for repo in repos:
                self.run_for_repo(ip_address, repo)

    def kill(self, param):
        pass


