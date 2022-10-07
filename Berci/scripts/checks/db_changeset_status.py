import psycopg2
from tabulate import tabulate

import utils
from Cluster import Cluster
from Repository import Repository
from sql_runner.parallel_runner.main import parallel_run
from utils import password_from_file, get_env


def get_changelogs(host, port, db, return_dict):
    conn = psycopg2.connect(
        host=host,
        port=port,
        database=db,
        user="postgres",
        password=utils.password_from_file('postgres', host, port)
    )

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
    return_dict[db] = num
    cur.close()
    conn.commit()
    conn.close()


if __name__ == '__main__':
    header = []
    result_d = {}
    result_l = []
    for port in range(5433, 5439):
        host = 'localhost'
        header.append(get_env(port))
        cluster = Cluster(host=host, port=port, passw=password_from_file('postgres', host, port))
        #databases = load_from_file('../databases.txt')
        databases = cluster.databases[0:]
        #databases = ['payment_psp_clearing']
        return_dict = parallel_run(host, port, databases, get_changelogs)
        for key, data in return_dict.items():
            if key not in result_d:
                result_d[key] = [data]
            else:
                result_d[key].append(data)
        print(f"{get_env(port)}: OK")
    for i in result_d.items():
        result_l.append([i[0]])
        idx = len(result_l) - 1
        result_l[idx] += i[1]
    print(tabulate(result_l, headers=header))

