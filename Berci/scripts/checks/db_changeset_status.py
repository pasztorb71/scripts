import re

import psycopg2
from tabulate import tabulate

import utils
from Repository import Repository
from sql_runner.parallel_runner.main import parallel_run
from utils import get_env
from utils_repo import get_repos_containing_release


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


def get_changeset_ids_from_repos_release(repos, release):
    out = {}
    for repo in repos:
        dir = Repository(repo).get_tables_dir()
        schema_file = f'{dir}/schema-version-0.xml'
        with open(schema_file, 'r', encoding='utf8') as f:
            if release:
                files = [(re.match('.*file="(.*)" relat.*labels="(.*)"/>', line).group(1),
                           re.match('.*file="(.*)" relat.*labels="(.*)"/>', line).group(2))
                          for line in f.readlines() if release in line]
            else:
                files = [(re.match('.*file="(.*)" relat.*labels="(.*)"/>', line).group(1),
                           re.match('.*file="(.*)" relat.*labels="(.*)"/>', line).group(2))
                         for line in f.readlines() if 'labels=' in line and 'debezium' not in line]

        d_files = {}
        for file in files:
            with open(f'{dir}/{file[0]}', 'r', encoding='utf8') as f:
                ids = [re.match('.*:(.*) run.*', line).group(1) for line in f.readlines() if line.startswith('--changeset')]
                d_files[f'{file[0]}||{file[1]}'] = ids
        out[repo] = d_files
    return out


def print_changeset(changeset_ids: dict, format='txt'):
    if format == 'csv':
        for repo, files in changeset_ids.items():
            for file, ids in files.items():
                for id in ids:
                    print(f'{repo};{id}')
    else:
        for repo, files in changeset_ids.items():
            print(repo)
            for file, ids in files.items():
                print('  '+'\n  '.join(ids))

def print_changeset1(changeset_ids):
    for repo, files in changeset_ids.items():
        print(repo)
        l_ids = []
        for file, ids in files.items():
            l_ids += [re.match('.*(MLFFDEV-.*)-.*', id).group(1) for id in ids]
        f = set(l_ids)
        print('  '+'\n  '.join(f))
        pass

if __name__ == '__main__':
    """
    release = 'R0.10'
    repos = get_repos_containing_release(release)
    changeset_ids = get_changeset_ids_from_repos_release(repos, release)
    print_changeset(changeset_ids, format='txt')
    #print_changeset1(changeset_ids)
    #check_
    exit(0)
    """
    version_files = {}
    result_d = {}
    result_l = []
    databases = utils.get_all_databases('sandbox')
    result_arr = [[None] * 3] * 10
    ports = range(5433, 5434)
    header = []
    for port in ports:
        header.append(get_env(port))
    host = 'localhost'
    #version_files = get_version_filenames(databases, '0.08')
    databases = ['core_vehicle']
    return_dict = parallel_run(host, ports, databases, get_changelogs)
    for key, data in return_dict.items():
        if key not in result_d:
            result_d[key] = [data]
        else:
            result_d[key].append(data)
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

