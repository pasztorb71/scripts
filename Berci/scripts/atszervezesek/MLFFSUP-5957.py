import os

from utils.utils_db import get_db_name
from utils.utils_file import copy_file, copy_dir, append_to_file_after_line_last_occurence, replace_in_file


def sema_atszervezes(repos):
  src_repo = "C:/GIT/MLFF/mlff-core-customer-postgredb/"
  for repo in repos[0:]:
    base_new = 'c:/GIT/MLFF/' + repo + '/liquibase/'
    db = get_db_name(base_new)
    dst_repo = base + repo.split('.')[0] + '/'

    filename = "ddl_changes_module.xml"
    src_dirpath = src_repo + 'liquibase/core_customer/ddl_changes_module/'
    dst_dirpath = dst_repo + 'liquibase/' + db + '/ddl_changes_module/'
    copy_file(src_dirpath + filename, dst_dirpath + filename)

    filename = "grant_read_privileges_to_stream_user.sql"
    copy_file(src_dirpath + filename, dst_dirpath + filename)


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    repos = os.listdir(base)
    repos = [x for x in os.listdir(base) if 'customer' not in x]
    sema_atszervezes(repos)
