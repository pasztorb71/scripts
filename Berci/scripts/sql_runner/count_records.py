import Environment
from sql_runner.parallel_runner.main import gen_port_databases_from_envs

if __name__ == '__main__':
    envs = Environment.get_envs()[1:-1] #local nem kell, mlff_test nem kell
    print(envs)
    ports_databases = gen_port_databases_from_envs(envs[0:], forced_refresh=False)[0:]
    print(ports_databases)
