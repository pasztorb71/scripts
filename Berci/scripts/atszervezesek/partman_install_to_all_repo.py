import os

from utils.utils_db import get_db_name
from utils.utils_file import copy_file, copy_dir, append_to_file_after_line_last_occurence, replace_in_file


def sema_atszervezes(repos):
  src_repo = "C:/GIT/MLFF/mlff-enforcement-eligibility-postgredb/"
  for repo in repos[0:1]:
    base_new = 'c:/GIT/MLFF/' + repo + '/liquibase/'
    db = get_db_name(base_new)
    dst_repo = base + repo.split('.')[0] + '/'

    filename = "etc/release/Dockerfile"
    copy_file(src_repo + filename, dst_repo + filename)

    dirpath = 'liquibase/partman_custom'
    copy_dir(src_repo + dirpath, dst_repo + dirpath, delete_dir_if_exists=True)

    replace_in_file(base_new + db + '/liquibase-install-db1-step-01.xml',
                    [["""    <include file="_create_dbs/create-database-db1.sql" relativeToChangelogFile="true"/>
""",
                    """    <include file="_create_dbs/create-database-db1.sql" relativeToChangelogFile="true"/>

    <!-- =================================================================================== -->
    <!-- Cron jobok inicializálása                                          -->
    <!-- =================================================================================== -->
    <include file="cron_jobs/init_cron_jobs.sql" relativeToChangelogFile="true"/>
"""]])

    src_dirpath = 'liquibase/enforcement_eligibility/cron_jobs'
    dst_dirpath = 'liquibase/' + db + '/cron_jobs'
    copy_dir(src_repo + src_dirpath, dst_repo + dst_dirpath, delete_dir_if_exists=True)

    src_dirpath = 'liquibase/enforcement_eligibility/cron_jobs'
    dst_dirpath = 'liquibase/' + db + '/cron_jobs'
    copy_dir(src_repo + src_dirpath, dst_repo + dst_dirpath, delete_dir_if_exists=True)

    replace_in_file(base_new + db + '/liquibase-install-db1-step-02.xml',
                    [["""    <include file="./create_publication.sql" relativeToChangelogFile="true"/>
""",
                    """    <include file="./create_publication.sql" relativeToChangelogFile="true"/>

    <!-- =================================================================================== -->
    <!-- A Extension-ök telepítése..                                                         -->
    <!-- =================================================================================== -->
    <include file="create_extensions.sql" relativeToChangelogFile="true"/>
"""]])

    filename = "create_extensions.sql"
    src_dirpath = src_repo + 'liquibase/enforcement_eligibility/'
    dst_dirpath = dst_repo + 'liquibase/' + db + '/'
    copy_file(src_dirpath + filename, dst_dirpath + filename)

    replace_in_file(base_new + db + '/liquibase-install-db1-step-02.xml',
                    [["""    <include file="ddl_changes_module/ddl_changes_module.xml" relativeToChangelogFile="true"/>
""",
                    """    <include file="ddl_changes_module/ddl_changes_module.xml" relativeToChangelogFile="true"/>

    <!-- =================================================================================== -->
    <!-- PARTMAN installálása..                                                              -->
    <!-- =================================================================================== -->
    <include file="partman/prepare_partman_schema.sql" relativeToChangelogFile="true"/>
    <include file="../partman_custom/liquibase-install-partman.xml" relativeToChangelogFile="true"/>
    <include file="partman/partman_grants.sql" relativeToChangelogFile="true"/>
"""]])
    src_dirpath = 'liquibase/enforcement_eligibility/partman'
    dst_dirpath = 'liquibase/' + db + '/partman'
    copy_dir(src_repo + src_dirpath, dst_repo + dst_dirpath, delete_dir_if_exists=True)


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    repos = os.listdir(base)
    repos = [x for x in os.listdir(base) if 'ion-image-postg' in x]
    sema_atszervezes(repos)
