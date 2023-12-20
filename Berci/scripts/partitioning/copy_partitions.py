from utils.utils_file import copy_file, replace_in_file


def get_schema_version_lines(file):
    with open (file, 'r') as f:
        return [l.split('"')[1] for l in f.readlines() if '<include' in l]

if __name__ == '__main__':
    dstdir = 'c:/GIT/MLFF/mlff-settlement-tro-clearing-postgredb/liquibase/settlement_tro_clearing/tro_clearing/tables/'
    file = dstdir + 'schema-version-022.xml'
    files = get_schema_version_lines(file)
    srcfile = 'c:/GIT/MLFF/mlff-payment-account-info-postgredb/liquibase/payment_account_info/account_info/tables/user_data/0213-user_data$hist-DDL.sql'
    for file in files:
        fname = file.split('/')[0]
        copy_file(srcfile, dstdir + file)
        replace_in_file(dstdir + file, [['USER_DATA', fname.upper()], ['user_data', fname], ['account_info', 'tro_clearing']])