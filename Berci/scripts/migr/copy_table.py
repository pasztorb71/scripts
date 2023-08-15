from Gcloud import list_sql_databases, get_instance_email


def gen_bucket_write_rights(project, instances) -> list:
    print('start gen_bucket_write_rights...')
    out = []
    for instance in instances:
        print(instance)
        email = get_instance_email(project, instance)
        out.append(f'gsutil iam ch serviceAccount:{email}:roles/storage.objectCreator gs://backup-teszt')
    out.append('')
    return out


def read_parameters():
    #TODO migr-read_parameters

if __name__ == '__main__':
    a,b,c = read_parameters()
    project = 'cantas-dev-id'
    outdir = 'c:/Users/bertalan.pasztor/Documents/MLFF/Partitioning_test/'
    filename = 'payment_export.bat'
    commands = [f'gcloud config set project {project}\n']
    #instances = [x for x in list_sql_instances(project, 'mskl') if '-data-' not in x and '-user-' not in x]
    #instances = ['pg-doc-mqid', 'pg-eobu-mqid', 'pg-core-mqid', 'pg-payment-mqid', 'pg-settlement-mqid',
    #             'pg-obu-mqid', 'pg-enforcement-mqid']
    instances = ['pg-payment-wbcv']
    commands += gen_bucket_write_rights(project, instances)
    print('generate export commands...')
    for instance in instances:
        print(instance)
        email = get_instance_email(project, instance)
        dblist = list_sql_databases(project, instance)
        for db in dblist:
            commands.append(f'gcloud sql export sql {instance} gs://backup-teszt/{db}.gz --database={db}')
    with open(f'{outdir}{filename}', 'w') as f:
        f.write('\n'.join(commands))

