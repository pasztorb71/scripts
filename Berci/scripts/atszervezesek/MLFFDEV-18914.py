import os
import shutil

import Repository
from utils import utils_file
from utils.utils_db import get_db_name, get_schema, get_sema_from_dbname
from utils.utils_file import del_file_ignore_error

env_template = """
MLFF_LIQUIBASE_COMMON_IMAGE=${DOCKER_REPOSITORY}/liquibase/mlff-liquibase-common-postgredb
MLFF_LIQUIBASE_COMMON_VERSION=0.1.0-SNAPSHOT

PARTMAN_CUSTOM_IMAGE=dockerhub.icellmobilsoft.hu/pg_partman_custom
PARTMAN_CUSTOM_VERSION=4.7.3-SNAPSHOT

DOCKER_DBNAME=$dbname
DOCKER_SERVNAME=$semaname

#liquibase, postgres és pg_tools verzió
DBDWH_IMAGE_VERSION=0.9.0
"""
def sema_atszervezes(repos):
  for repo in repos[0:]:
  # prepare
    _base = 'c:/GIT/MLFF/' + repo
    base = _base +'/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    schema = get_sema_from_dbname(db_path)
    to_replace = [['core-customer', db],['core_customer', db_path], ['customer', schema]]

    print(repo)
    #env mod
    utils_file.append_to_file_after_line_last_occurence(
          fname=_base + '/.env',
          after='DOCKER_LIQUIBASE_',
          what=env_template.replace('$dbname', db). replace('$semaname', schema)
    )
    #development.adoc
    utils_file.append_to_file_after_line_last_occurence(
          fname=_base + '/docs/development.adoc',
          after='rendszeresen elmarad.',
          what="""
=== Liquibase scriptek futtatása egy lépésben
a projekt könyvtárban állva
[source,bash]
----
docker-compose --env-file .env -f etc/docker-compose/docker-compose.yml up --build --force-recreate --scale liquibase-release=0
----"""
    )
    #release/docker-compose.yml
    utils_file.append_to_file_after_line_last_occurence(
          fname=_base + '/etc/release/docker-compose.yml',
          after='LIQUIBASE_INSTALL_DIR:',
          what="""        LIQUIBASE_COMMON_IMAGE: "$MLFF_LIQUIBASE_COMMON_IMAGE:$MLFF_LIQUIBASE_COMMON_VERSION"
        PARTMAN_CUSTOM_IMAGE: "$PARTMAN_CUSTOM_IMAGE:$PARTMAN_CUSTOM_VERSION"
        DBNAME: "$DOCKER_DBNAME"
        SERVNAME: "$DOCKER_SERVNAME" """
    )
    utils_file.replace_in_file(
            _base + '/etc/release/docker-compose.yml',
            [['dockerhub-mlff-group.icellmobilsoft.hu/liquibase:0.5.0',
              'dockerhub.icellmobilsoft.hu/db-dwh/liquibase:0.5.0']]
    )

    #Dockerfiles
    utils_file.copy_file("C:/GIT/MLFF/mlff-payment-account-info-postgredb/etc/release/Dockerfile", _base + '/etc/release/Dockerfile')
    utils_file.copy_file("C:/GIT/MLFF/mlff-payment-account-info-postgredb/etc/docker-compose/Dockerfile", _base + '/etc/docker-compose/Dockerfile')

    #install parameters
    utils_file.append_to_file_after_line_last_occurence(
            fname=base + db_path + '/install-parameters-db1.xml',
            after='"service_name"',
            what="""    <property name="schema_name"    value="account_info"/>""".replace('account_info', schema)
    )

    #compose/docker-compose
    to_replace = [
       ['payment-account-info', db]
      ,['payment_account_info', db_path]
      ,['account-info', schema]
    ]
    utils_file.copy_file_and_replace(
            "C:/GIT/MLFF/mlff-payment-account-info-postgredb/etc/docker-compose/docker-compose.yml",
            _base + '/etc/docker-compose/docker-compose.yml',
            to_replace)

    #remove files,dirs - database level
    shutil.rmtree(base + 'partman_custom', ignore_errors=True)
    del_file_ignore_error(base + db_path + '/create_extensions.sql')
    del_file_ignore_error(base + db_path + '/create_publication.sql')
    del_file_ignore_error(base + db_path + '/liquibase-install-db1-step-01.xml')
    del_file_ignore_error(base + db_path + '/liquibase-install-db1-step-02.xml')
    shutil.rmtree(base + db_path + '/__init_dbs', ignore_errors=True)
    shutil.rmtree(base + db_path + '/_all-modules', ignore_errors=True)
    shutil.rmtree(base + db_path + '/_create_dbs', ignore_errors=True)
    shutil.rmtree(base + db_path + '/cron_jobs', ignore_errors=True)
    shutil.rmtree(base + db_path + '/ddl_changes_module', ignore_errors=True)
    shutil.rmtree(base + db_path + '/partman', ignore_errors=True)


    # remove files,dirs - schema level
    shutil.rmtree(base + db_path + '/' + schema + '/schema')
    del_file_ignore_error(base + db_path + '/' + schema + '/install-modules.xml')
    del_file_ignore_error(base + db_path + '/' + schema + '/liquibase-install-schema.xml')


def sema_atszervezes_fix(repos):
  for repo in repos[0:]:
  # prepare
    _base = 'c:/GIT/MLFF/' + repo
    base = _base +'/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('_', '-')
    print(repo)
    # compose/docker-compose
    utils_file.replace_in_file(
          _base + '/etc/docker-compose/docker-compose.yml',
          [[f'mlff-{db}-postgredb:',
            f'mlff-{db_path}-postgredb:']]
    )

def common_egyszerusites(repos):
  for repo in repos[0:]:
  # prepare
    _base = 'c:/GIT/MLFF/' + repo
    base = _base +'/liquibase/'
    db_underscore = get_db_name(base)
    db_minus = db_underscore.replace('_', '-')
    schema = get_sema_from_dbname(db_underscore)
    if not schema:
      raise Exception(f'{db_underscore} : no schema')
    print(repo)
    # run.sh
    utils_file.replace_in_file(_base + '/run.sh', [[f'liquibase-install-db1-', f'liquibase-install-']])

    # Dockerfiles
    utils_file.copy_file("C:/GIT/MLFF/mlff-core-analytic-postgredb/etc/release/Dockerfile",
                         _base + '/etc/release/Dockerfile')
    utils_file.copy_file("C:/GIT/MLFF/mlff-core-analytic-postgredb/etc/docker-compose/Dockerfile",
                         _base + '/etc/docker-compose/Dockerfile')

    #properties files
    utils_file.replace_in_file(
            _base + f'/etc/docker-compose/config/{db_underscore}/step-01/liquibase-localhost.properties'
            ,[['liquibase-install-db1-step-01.xml'
            ,'liquibase-install-step-01.xml']])

    utils_file.replace_in_file(
            _base + f'/etc/docker-compose/config/{db_underscore}/step-02/liquibase-localhost.properties'
            , [['liquibase-install-db1-step-02.xml'
                 , 'liquibase-install-step-02.xml']])

    #schema-versions
    utils_file.copy_file("C:/GIT/MLFF/mlff-core-analytic-postgredb/liquibase/core_analytic/analytic/schema-versions.xml",
                         base + f'{db_underscore}/{schema}/schema-versions.xml')

    #schema-version-0
    utils_file.replace_in_file(
            base + f'{db_underscore}/{schema}/tables/schema-version-0.xml',
            [["""    <!-- =================================================================================== -->
    <!-- A Kafka replikáció működéséhez szükséges debezium segédtáblák létrehozása..         -->
    <!-- =================================================================================== -->
    <include file="../../_all-modules/schema/tables/debezium_heartbeat/debezium_heartbeat.sql" relativeToChangelogFile="true"/>
    <include file="../../_all-modules/schema/tables/dbz_signal/dbz_signal.sql" relativeToChangelogFile="true"/>

""".replace('\n', '\r\n'), '']])

  #install-parameters-db1.xml
    os.rename(base + f'{db_underscore}/install-parameters-db1.xml',
              base + f'{db_underscore}/install-parameters.xml')


if __name__ == '__main__':
    repos = Repository.Repository().get_repo_names_exclude(['analytic','inspection'])[1:2]
    #sema_atszervezes(repos)
    #sema_atszervezes_fix(repos)
    common_egyszerusites(repos)
