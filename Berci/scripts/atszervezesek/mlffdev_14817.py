import os

from utils import utils_file, utils_db
from Repository import Repository


def sema_atszervezes(repos):
    for repo in repos[0:]:
        print(repo)
        db = utils_db.get_db_name(repo)
        db_path = db.replace('-', '_')
        schema = Repository(repo).get_schema()
        utils_file.move_file(f'{base}{repo}/liquibase/{db_path}/__init_dbs/create_publication.sql',
                             f'{base}{repo}/liquibase/{db_path}/create_publication.sql')
        utils_file.append_to_file_after_line_last_occurence(f'{base}{repo}/liquibase/{db_path}/liquibase-install-db1-step-02.xml',
                                                            'databasechangelog-DDL-001.sql', """
    <!-- =================================================================================== -->
    <!-- A publication behivatkozása..                                          -->
    <!-- =================================================================================== -->
    <include file="./create_publication.sql" relativeToChangelogFile="true"/>""")

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    repos = [x for x in os.listdir(base) if 'onsite-alert-subscribe' not in x][1:]
    sema_atszervezes(repos)
