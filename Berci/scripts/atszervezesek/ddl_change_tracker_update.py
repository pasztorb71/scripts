import os

from utils.utils_db import get_db_name
from utils.utils_file import copy_file, copy_dir, append_to_file_after_line_last_occurence, replace_in_file, \
    get_line_from_file_by_linepart


def sema_atszervezes(repos, ticket):
  for repo in repos[0:]:
    base_new = 'c:/GIT/MLFF/' + repo + '/liquibase/'
    db = get_db_name(base_new)
    dst_repo = base + repo.split('.')[0] + '/'

    filename = "initial_load.sql"
    dst_dirpath = dst_repo + 'liquibase/' + db + '/ddl_changes_module/'
    filepath = dst_dirpath + filename
    line = get_line_from_file_by_linepart(filepath, 'RUN_INITIAL_LOAD')
    replace_in_file(dst_dirpath + filename,
                    [[line,
                    f"""--changeset bertalan.pasztor:RUN_INITIAL_LOAD-{ticket} endDelimiter:/\n"""]])

    filename = "f_log_ddl.sql"
    dst_dirpath = dst_repo + 'liquibase/' + db + '/ddl_changes_module/functions/'
    filepath = dst_dirpath + filename
    with open('C:/GIT/postgres_ddl_change_tracker/code/functions/f_log_ddl.sql', 'r') as inf:
        fromdata = inf.read()
    with open(filepath, 'w') as outf:
        outf.write(f"""--liquibase formatted sql

---------------------------------------------------------------------------------------------------
--changeset bertalan.pasztor:CREATE_F_LOG_DDL-{ticket} runOnChange:true stripComments:false endDelimiter:/
--comment Create f_log_ddl function.
---------------------------------------------------------------------------------------------------
""")
        outf.write(fromdata)
        outf.write('\n/\n')

    filename = "et_log_ddl_drop_info.sql"
    dst_dirpath = dst_repo + 'liquibase/' + db + '/ddl_changes_module/event_triggers/'
    filepath = dst_dirpath + filename
    line = get_line_from_file_by_linepart(filepath, 'CREATE_TRIGGER_ET_LOG_DDL_DROP_INFO')
    replace_in_file(dst_dirpath + filename,
                    [[line,
                    f"""--changeset bertalan.pasztor:CREATE_TRIGGER_ET_LOG_DDL_DROP_INFO-{ticket}\n"""]])

    filename = "et_log_ddl_info.sql"
    dst_dirpath = dst_repo + 'liquibase/' + db + '/ddl_changes_module/event_triggers/'
    filepath = dst_dirpath + filename
    line = get_line_from_file_by_linepart(filepath, 'CREATE_TRIGGER_ET_LOG_DDL_INFO')
    replace_in_file(dst_dirpath + filename,
                    [[line,
                    f"""--changeset bertalan.pasztor:CREATE_TRIGGER_ET_LOG_DDL_INFO-{ticket}\n"""]])


if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    ticket = 'MLFFSUP-6252'
    repos = os.listdir(base)
    repos = [x for x in os.listdir(base) if 'analytic' not in x]
    sema_atszervezes(repos, ticket)
