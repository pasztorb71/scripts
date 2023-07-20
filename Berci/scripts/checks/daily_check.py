from sql_runner.parallel_runner.main import gen_port_databases_from_envs


def main():
    check_partition_privileges()


def check_partition_privileges():
    env = 'train'
    # databases = load_from_file('../databases.txt')
    # databases = ['core_customer']
    ports_databases = gen_port_databases_from_envs(env)[0:]
    # ports_databases = [[5741, 'postgres']]
    # return_dict = parallel_run(ports_databases, mproc_count_records)
    return_dict = parallel_run_sql(ports_databases, hash_in_fk, mproc_single_sql)


main()