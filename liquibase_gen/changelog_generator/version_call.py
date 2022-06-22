from utils import get_repo_from_schema


class Version_call:
    def __init__(self, version, schema):
        self.version = version
        self.schema = schema
        self.repo = get_repo_from_schema(schema)

    #TODO
    def tmp_version_call(self, schema, table):
        base = 'c:/GIT/MLFF/'
        repo = get_repo_from_schema(schema)
        path = base+repo+'/liquibase/'+os.listdir(base+repo+'/liquibase')[0]+'/'+schema
        a = 1
