import glob
import os


def _runner(base, project, type, env, postgrespass, db='', file=''):
    install_database = '''docker run --rm -v #base##project#\:/liquibase/changelog liquibase/liquibase:4.7 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/postgres --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=liquibase-install-databases.xml update'''
    install_schema = '''docker run --rm -v #base##project#\:/liquibase/changelog liquibase/liquibase:4.7 --logLevel=info --liquibase-hub-mode=off --url=jdbc:postgresql://#env#/#db# --driver=org.postgresql.Driver --username=postgres --password=#password# --classpath=/liquibase/changelog --changeLogFile=liquibase-install-#db#.xml update'''
    if type == 'db':
        cmd = install_database
        cmd = cmd\
            .replace('#base#', base)\
            .replace('#project#', project)\
            .replace('#env#', env)\
            .replace('#password#', postgrespass)
    elif type == 'schema':
        cmd = install_schema
        cmd = cmd\
            .replace('#base#', base)\
            .replace('#project#', project)\
            .replace('#env#', env)\
            .replace('#password#', postgrespass)\
            .replace('#db#', db)
    print(cmd)
    ret_code = os.system(cmd)
    if ret_code != 0:
        exit(ret_code)


def get_dbs(base, repo):
    dblist = []
    path = base + repo + '/*.xml'
    print(path)
    files = glob.glob(path)
    files = [f.split('\\')[1] for f in files if 'liquibase-install-databases.xml' not in f]
    dblist = [file.replace('liquibase-install-','').replace('.xml','') for file in files]
    return dblist


def runner(repos, loc):
    ip_addresses = ['gateway.docker.internal:5433', 'gateway.docker.internal:5434'] if loc == 'remote' else ['gateway.docker.internal']
    for ip_address in ip_addresses:
        for repo in repos:
            repo = repo + '/liquibase' if os.path.isdir(base + repo + '/liquibase') else repo
            print(repo)
            _runner(base, repo, 'db', ip_address, 'fLXyFS0RpmIX9uxGII4N')
            dbs = get_dbs(base, repo)
            for db in dbs:
                _runner(base, repo, 'schema', ip_address, 'fLXyFS0RpmIX9uxGII4N', db)


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    repos = ['mlff-payment-transaction-postgredb']
    runner(repos, loc='remote')
