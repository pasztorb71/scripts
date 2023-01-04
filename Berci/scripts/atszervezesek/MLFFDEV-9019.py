import os

import utils
import utils_db
import utils_file
from Repository import Repository


def sema_atszervezes(repos):
    for repo in repos[1:]:
        print(repo)
        db = utils_db_schema.get_db_name(repo)
        db_path = db.replace('-', '_')
        schema = Repository(repo).get_schema()
        to_replace = [['core-customer', db], ['core_customer', db_path]]
        utils_file.copy_file(base + src + '/liquibase/core_customer/_all-modules/schema/refresh_table_roles.sql',
                             base + repo +'/liquibase/' + db_path +'/_all-modules/schema/refresh_table_roles.sql')
        utils_file.copy_file(base + src + '/liquibase/core_customer/_all-modules/schema/procedures/add_privileges_to_all_tables.sql',
                             base + repo +'/liquibase/' + db_path +'/_all-modules/schema/procedures/add_privileges_to_all_tables.sql')
        utils_file.copy_file(base + src + '/liquibase/core_customer/_all-modules/schema/procedures/add_privileges_to_table.sql',
                             base + repo +'/liquibase/' + db_path +'/_all-modules/schema/procedures/add_privileges_to_table.sql')
        utils_file.append_to_file_after_line_last_occurence(base + repo + '/liquibase/' + db_path + '/' + schema + '/schema-versions.xml',
                                                       'schema-version-0.xml',
                                                       '    <!--<include file="tables/schema-version-1.xml" relativeToChangelogFile="true"/>-->')
        utils_file.append_to_file_after_line_last_occurence(base + repo + '/liquibase/' + db_path + '/' + schema + '/schema-versions.xml',
                                                       '<!-- ================',
                                                       """    <!-- A tábla jogok frissítése, létrehozások, és változások után, mindig itt a legvégén!  -->
    <!-- =================================================================================== -->
    <include file="../_all-modules/schema/refresh_table_roles.sql" relativeToChangelogFile="true"/>
    <!-- =================================================================================== -->""")
        continue
        utils_file.copy_file_and_replace(base + src + '/run.sh', base + repo + '/run.sh', to_replace)
        os.system(f'wsl ~ -e sh -c "dos2unix /mnt/c/GIT/MLFF/{repo}/run.sh"')
        os.system('git -C ' + base+repo + ' add ' + base+repo+'/run.sh')
        os.system('git -C '+base+repo+' update-index --chmod=+x '+base+repo+'/run.sh')
        utils_file.copy_file_and_replace(base + src + '/README.adoc', base + repo + '/README.adoc', to_replace)


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    src = 'mlff-core-customer-postgredb'
    repos = [x for x in os.listdir(base) if 'core-customer' not in x]
    #repos = ['mlff-data-ingestion-meta-postgredb']
    sema_atszervezes(repos)
