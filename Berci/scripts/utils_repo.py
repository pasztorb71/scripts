import Repository
from utils_file import file_contains


def get_instance_from_repo_full_name(repo):
    if repo == 'doc-postgredb':
        return 'pg-doc-mqid'
    else:
        id = repo.split('-')[1]
        return 'pg-' + id + '-mqid'


def get_repos_containing_release(rname):
    out = []
    for repo in Repository().get_repo_names():
        if file_contains(f'{Repository(repo).get_tables_dir()}/schema-version-0.xml', rname):
            out.append(repo)
    return out


