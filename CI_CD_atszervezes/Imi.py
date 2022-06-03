import os
import re

from CI_CD_atszervezes.utils import copy_dir


def _cre_docker_compose_build(fname):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(""".docker-compose-build:
  build-push:
    - docker-compose --env-file .env -f etc/release/docker-compose.yml build
    - !reference [.docker-script, test]
    - etc/release/release.sh
    - !reference [.docker-script, test]
""")

def create_file(fname):
    if 'docker-compose-build.yml' in fname:
        _cre_docker_compose_build(fname)

if __name__ == '__main__':
    repo = 'mlff-core-vehicle-postgredb'
  # prepare
    #copy_dir('c:/GIT/MLFF/' + repo, 'c:/GIT/MLFF/' + repo + ' másolata')
    base = 'c:/GIT/MLFF/' + repo + ' másolata/'

    os.makedirs(base+'.gitlab/release', exist_ok=True)
    create_file(base+'.gitlab/release/docker-compose-build.yml')
