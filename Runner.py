import glob
import os


class Runner:
    def __init__(self, base):
        self.base = base

    def _runner(self, project, type, env, postgrespass, db='', file=''):
        install_database = '''docker run --rm -v #base##project#\:/liquibase/changelog liquibase/liquibase:4.7 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/postgres --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=liquibase-install-databases.xml update'''
        install_schema = '''docker run --rm -v #base##project#\:/liquibase/changelog liquibase/liquibase:4.7 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/#db# --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=liquibase-install-#db#.xml update'''
        if type == 'db':
            cmd = install_database
            cmd = cmd\
                .replace('#base#', self.base)\
                .replace('#project#', project)\
                .replace('#env#', env)\
                .replace('#password#', postgrespass)
        elif type == 'schema':
            cmd = install_schema
            cmd = cmd\
                .replace('#base#', self.base)\
                .replace('#project#', project)\
                .replace('#env#', env)\
                .replace('#password#', postgrespass)\
                .replace('#db#', db)
        print(cmd)
        ret_code = os.system(cmd)
        if ret_code != 0:
            exit(ret_code)


    def get_dbs(self, repo):
        dblist = []
        path = self.base + repo + '/*.xml'
        print(path)
        files = glob.glob(path)
        files = [f.split('\\')[1] for f in files if 'liquibase-install-databases.xml' not in f]
        dblist = [file.replace('liquibase-install-','').replace('.xml','') for file in files]
        return dblist

    def get_ip_addresses(self, loc):
        return ['gateway.docker.internal:5433', 'gateway.docker.internal:5434'] if loc == 'remote' else [
            'gateway.docker.internal']

    def run(self, repos, loc):
        for ip_address in self.get_ip_addresses(loc):
            for repo in repos:
                print(repo)
                repo = repo + '/liquibase'
                self._runner(repo, 'db', ip_address, 'fLXyFS0RpmIX9uxGII4N')
                dbs = self.get_dbs(repo)
                for db in dbs:
                    self._runner(repo, 'schema', ip_address, 'fLXyFS0RpmIX9uxGII4N', db)


