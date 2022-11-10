import os

import utils
import utils_db_schema
import utils_file


def sema_atszervezes(repos):
    for repo in repos[0:]:
        db = utils_db_schema.get_db_name(repo)
        db_path = db.replace('-', '_')
        to_replace = [['core-customer', db], ['core_customer', db_path]]
        utils_file.copy_file(base + src + '/etc/release/Dockerfile', base + repo + '/etc/release/Dockerfile')
        utils_file.copy_file_and_replace(base + src + '/run.sh', base + repo + '/run.sh', to_replace)
        os.system(f'wsl ~ -e sh -c "dos2unix /mnt/c/GIT/MLFF/{repo}/run.sh"')
        os.system('git -C ' + base+repo + ' add ' + base+repo+'/run.sh')
        os.system('git -C '+base+repo+' update-index --chmod=+x '+base+repo+'/run.sh')
        utils_file.copy_file_and_replace(base + src + '/README.adoc', base + repo + '/README.adoc', to_replace)


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    src = 'mlff-core-customer-postgredb'
    fromdb = utils_db_schema.get_dbname_from_project(src)
    fromdb1 = utils_db_schema.get_db_name(src)
    repos = [x for x in os.listdir(base) if 'core-customer' not in x]
    repos = ['mlff-data-ingestion-meta-postgredb']
    sema_atszervezes(repos)
