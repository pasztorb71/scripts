from utils import copy_file_and_replace, replace_in_file, load_from_file, append_to_file_after_line


def sema_atszervezes(repos):
  def is_needed(repo):
    return repo not in ['mlff-core-customer-postgredb']
  for repo in repos[0:]:
  # prepare
    base = 'c:/GIT/MLFF/'+repo+'/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    if not is_needed(repo): continue

    #git_init(move_upper_dir(base))
    schema = get_schema(base, db_path)
    to_replace = [['schema_name_'+schema, 'schema_name']]
    to_replace_customer = [['core-customer', db], ['core_customer', db_path], ['customer', schema]]

    print(repo)
  #stream user
    path = base+db_path+'/_init_dbs/'
    append_to_file_after_line(
      fname=path + db_path + '-db-install.xml',
      after='service-user.sql',
      what='    <include file="'+db_path+'/'+schema+'/stream-user.sql" relativeToChangelogFile="true"/>'
    )
    path = base+db_path+'/'+schema+'/schema/'
    append_to_file_after_line(
      fname=path+'install-schema.xml',
      after='service-user.sql',
      what='    <include file="alter-stream-user.sql" relativeToChangelogFile="true"/>'
    )
    copy_file_and_replace('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/_init_dbs/core_customer/customer/stream-user.sql',
                          base+db_path+'/_init_dbs/'+db_path+'/'+schema+'/stream-user.sql',
                          to_replace_customer)

    copy_file_and_replace('c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/customer/schema/alter-stream-user.sql',
                          base+db_path+'/'+schema+'/schema/alter-stream-user.sql',
                          to_replace_customer)
  #readonly userek
    path = base + db_path + '/_init_dbs/'
    append_to_file_after_line(
      fname=path + db_path + '-db-install.xml',
      after='stream-user.sql',
      what='    <include file="' + db_path + '/' + schema + '/dwh-read-user.sql" relativeToChangelogFile="true"/>'
    )
    append_to_file_after_line(
      fname=path + db_path + '-db-install.xml',
      after='dwh-read-user.sql',
      what='    <include file="' + db_path + '/' + schema + '/read-user.sql" relativeToChangelogFile="true"/>'
    )
    path = base + db_path + '/' + schema + '/schema/'
    replace_in_file(path+'create-schema.sql',[['_full', '_sel']])
    append_to_file_after_line(
      fname=path + 'install-schema.xml',
      after='alter-stream-user.sql',
      what='    <include file="alter-read-user.sql" relativeToChangelogFile="true"/>'
    )
    append_to_file_after_line(
      fname=path + 'install-schema.xml',
      after='alter-read-user.sql',
      what='    <include file="alter-dwh-read-user.sql" relativeToChangelogFile="true"/>'
    )
    copy_file_and_replace(
      'c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/_init_dbs/core_customer/customer/read-user.sql',
      base + db_path + '/_init_dbs/' + db_path + '/' + schema + '/read-user.sql',
      to_replace_customer)
    copy_file_and_replace(
      'c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/_init_dbs/core_customer/customer/dwh-read-user.sql',
      base + db_path + '/_init_dbs/' + db_path + '/' + schema + '/dwh-read-user.sql',
      to_replace_customer)
    copy_file_and_replace(
      'c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/customer/schema/alter-read-user.sql',
      base + db_path + '/' + schema + '/schema/alter-read-user.sql',
      to_replace_customer)
    copy_file_and_replace(
      'c:/GIT/MLFF/mlff-core-customer-postgredb/liquibase/core_customer/customer/schema/alter-dwh-read-user.sql',
      base + db_path + '/' + schema + '/schema/alter-dwh-read-user.sql',
      to_replace_customer)

def sema_atszervezes_fix1(repos):
  def is_needed(repo):
    return repo not in ['mlff-core-customer-postgredb']
  for repo in repos[0:]:
  # prepare
    base = 'c:/GIT/MLFF/'+repo+'/liquibase/'
    db = get_db_name(base)
    db_path = db.replace('-', '_')
    if not is_needed(repo): continue

    #git_init(move_upper_dir(base))
    schema = get_schema(base, db_path)
    to_replace = [['schema_name_'+schema, 'schema_name']]
    to_replace_customer = [['core-customer', db], ['core_customer', db_path], ['customer', schema]]

    print(repo)

    path = base+db_path+'/_init_dbs/'


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    repos = load_from_file('repos.txt')
    #repos = [x for x in os.listdir(base) if x.startswith('mlff-enforcement')]
    repos = ['mlff-payment-retry-postgredb']
    sema_atszervezes(repos)
    sema_atszervezes_fix1(repos)

