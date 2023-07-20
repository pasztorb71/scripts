import os
import subprocess


def list_sql_instances(project: str, id_part: str) -> list[str]:
    os.system(f'gcloud config set project {project}')
    a = os.popen('gcloud sql instances list').readlines()[1:]
    return [x.split()[0] for x in a if id_part in x and '-replica' not in x ]

def list_sql_databases(project: str, instance: str) -> list[str]:
    os.system(f'gcloud config set project {project}')
    cmd = f'gcloud sql databases list --instance={instance}'
    #print(cmd)
    a = os.popen(cmd).readlines()[1:]
    return [x.split()[0] for x in a if 'postgres ' not in x ]

def get_instance_email(project: str, instance: str) -> list[str]:
    set_project(project)
    cmd = f'gcloud sql instances describe {instance}'
    #print(cmd)
    a = os.popen(cmd).readlines()
    emailrow = [x for x in a if 'serviceAccountEmailAddress' in x]
    return emailrow[0].split(': ')[1].replace('\n','')


def set_project(project):
    subprocess.run(f'gcloud config set project {project}', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)