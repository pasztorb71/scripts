import os

import utils
import utils_db
import utils_file
from Repository import Repository


def sema_atszervezes(repos):
    for repo in repos[0:]:
        print(repo)
        db = utils_db.get_db_name(repo)
        db_path = db.replace('-', '_')
        schema = Repository(repo).get_schema()
        #utils_file.copy_file('c:/GIT/MLFF/mlff-data-ingestion-meta-postgredb/liquibase/data_ingestion_meta/ingestion_meta/schema/default/alter-dwh_stream-user.sql',
        #                     f'{base}{repo}/liquibase/{db_path}/{schema}/schema/default/alter-dwh_stream-user.sql')
        utils_file.copy_file('c:/GIT/MLFF/mlff-payment-invoice-postgredb/liquibase/payment_invoice/invoice/liquibase-install-schema.xml',
                             f'{base}{repo}/liquibase/{db_path}/{schema}/liquibase-install-schema.xml')


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = [x for x in os.listdir(base) if 'ingestion-meta' not in x][0:]
    repos = [x for x in os.listdir(base) if 'invoice' not in x][0:1]
    sema_atszervezes(repos)
