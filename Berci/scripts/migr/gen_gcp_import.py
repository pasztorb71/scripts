from Gcloud import list_sql_databases, get_instance_email, set_project


def gen_bucket_write_rights(project, instances) -> list:
    out = []
    for instance in instances:
        print(instance)
        email = get_instance_email('mlff-sb', instance)
        out.append(f'gsutil iam ch serviceAccount:{email}:roles/storage.objectCreator gs://backup-teszt')
    return out


def gen_bucket_read_rights(project, instances) -> list:
    out = []
    for instance in instances:
        print(instance)
        email = get_instance_email(project, instance)
        out.append(f'gsutil iam ch serviceAccount:{email}:roles/storage.objectViewer gs://backup-teszt')
    return out


if __name__ == '__main__':
    project = 'mlff-sb-s'
    outdir = 'c:/Users/bertalan.pasztor/Documents/MLFF/Partitioning_test/'
    bucket = 'backup_cantas_dev'
    filename = 'payment_import.bat'
    commands = [f'gcloud config set project {project}\n']
    #instances = [x for x in list_sql_instances(project, '8h5k') if '-data-' not in x and '-user-' not in x]
    instances = ['mlff-db-perf-teszt']
    commands += gen_bucket_read_rights(project, instances)
    for instance in instances:
        print(instance)
        dblist = list_sql_databases(project, instance)
        for db in dblist:
            commands.append(f'gcloud sql import sql {instance} gs://backup-teszt/{db}.gz --database={db} --user=postgres -q')
    commands.append('\n')
    with open(f'{outdir}{filename}', 'w') as f:
        f.write('\n'.join(commands))

