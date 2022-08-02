import Repository
import utils
from liquibase_gen.changelog_generator.Ticket import Ticket


def create_schema_version(repo, version):
    #TODO make repo object for this and gen_table
    base = 'c:/GIT/MLFF/' + repo + '/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    schema = Repository.get_sema_from_dbname(db_path)
    #with open('/'.join[base,db_path,schema])
    schema_version_path = '/'.join([base+db_path,schema,'xml-version-tree/schema-version-0.xml'])
    with open(schema_version_path, 'r+', encoding='utf-8') as f:
        old = f.read().split()
        if not any(['version-0/'+version+'.xml' in x for x in old]):
            last_ver = max(index for index, item in enumerate(old) if '<include file="version-0/' in item)
        a = 1
    a = 1


if __name__ == '__main__':
    repo = 'mlff-core-notification-email-postgredb'
    version = Ticket('MLFFDEV-3858').get_version()
    create_schema_version(repo, version)
    a = 1


