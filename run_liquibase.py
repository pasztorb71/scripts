import glob
import os


def runner(base, project, type, env, postgrespass, db='', file=''):
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
    os.system(cmd)


def get_dbs(base, repo):
    dblist = []
    path = base + repo + '/*.xml'
    print(path)
    files = glob.glob(path)
    files = [f.split('\\')[1] for f in files if 'liquibase-install-databases.xml' not in f]
    dblist = [file.replace('liquibase-install-','').replace('.xml','') for file in files]
    return dblist


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    ip_addresses = ['gateway.docker.internal:5433', 'gateway.docker.internal:5434']
    #repos = os.listdir(base)
    repos = ['mlff-payment-transaction-postgredb']
    run = True
    for ip_address in ip_addresses:
        a = ''
        for repo in repos:
            repo = repo + '/liquibase' if os.path.isdir(base + repo + '/liquibase') else repo
            while a != 'y' and a != 'N' :
                a = 'y'
                print(repo)
                schemas = get_dbs(base, repo)
                runner(base, repo, 'db', ip_address, 'fLXyFS0RpmIX9uxGII4N')
                # = input('Tovább(y/N)')
                if a == 'N':
                    run = False
                    break
                dbs = get_dbs(base, repo)
                for db in dbs:
                    runner(base, repo, 'schema', ip_address, 'fLXyFS0RpmIX9uxGII4N', db)
                    #a = input('Tovább(y/N)')
                    if a == 'N':
                        run = False
                        break
            if not run:
                break