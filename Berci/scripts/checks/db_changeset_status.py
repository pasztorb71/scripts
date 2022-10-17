import re

import psycopg2
from tabulate import tabulate

import utils
from Cluster import Cluster
from Repository import Repository
from sql_runner.parallel_runner.main import parallel_run
from utils import password_from_file, get_env


def get_changelogs(host, port, db, return_dict):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            database=db,
            user="postgres",
            password=utils.password_from_file('postgres', host, port)
        )
    except psycopg2.OperationalError:
        return_dict[f'{db}|{port}'] = None
        return

    cur = conn.cursor()
    cur.execute("""SELECT DISTINCT * FROM (
SELECT COALESCE(labels, substring(id FROM 'DDL-(.*)-MLFFDEV')) st 
FROM databasechangelog d 
WHERE id LIKE '%DDL%'
) s
WHERE st IS NOT null
;""")
    record = cur.fetchall()
    if record:
        num = max([int(x[0].split('.')[1]) for x in record])
    else:
        num = 1
    return_dict[f'{db}|{port}'] = num
    cur.close()
    conn.commit()
    conn.close()


def get_version_filenames(databases, version):
    out = {}
    for db in databases:
        fnames = []
        fname = Repository(db.replace('_', '-')).get_tables_dir() + '/schema-version-0.xml'
        with open(fname, 'r', encoding='utf8') as f:
            for line in f.readlines():
                if f'labels="{version}"' in line:
                    fi = re.match('.*<include file="(.*)" relativeToChangelogFile.*', line).group(1)
                    fnames.append(fi)
        out[db] = fnames
    return out


def get_all_databases():
    cluster = Cluster(host='localhost', port=5433, passw=password_from_file('postgres', 'localhost', 5433))
    return cluster.databases[0:]


if __name__ == '__main__':
    """
    version_files = {}
    result_d = {}
    result_l = []
    """
    result_arr = [[None] * 3] * 10
    databases = get_all_databases()
    ports = range(5433, 5435)
    header = []
    for port in ports:
        header.append(get_env(port))
    host = 'localhost'
    #version_files = get_version_filenames(databases, '0.08')
    #databases = ['core_vehicle']
    return_dict = parallel_run(host, ports, databases, get_changelogs)
    """
    for key, data in return_dict.items():
        if key not in result_d:
            result_d[key] = [data]
        else:
            result_d[key].append(data)
    """
    print(return_dict)
    for key, data in return_dict.items():
        print(f'{key} {data}')
    exit(0)
    print(f"{get_env(port)}: OK")
    """
    for i in result_d.items():
        result_l.append([i[0]])
        idx = len(result_l) - 1
        result_l[idx] += i[1]
    """
    print(tabulate(result_l, headers=header))

