import Environment
from Repository import Repository
from liquibase_runner.Runner import Runner

repos = [Repository('customer')]


def gen_build_and_run_commands(repo):
    out = ''
    out += f'docker-compose --env-file c:/GIT/MLFF/{repo.name}/.env' \
           f' -f c:/GIT/MLFF/{repo.name}/etc/release/docker-compose.yml build\n\n'
    out += f"""docker run --rm \\
  -e DB_ADDRESS=gateway.docker.internal \\
  -e DB_PORT=5432 \\
  -e POSTGRES_PASSWORD=postgres \\
  dockerhub-mlff.icellmobilsoft.hu/liquibase/{repo.name}:{repo.env_ver}.0-SNAPSHOT"""
    return out

if __name__ == '__main__':
    repos = [Repository('-eligibility-pos')]
    #repos = [Repository(x) for x in Repository.get_repo_names() if '' in x][1:]
    '''
    '''
    Runner(repos)
    for repo in repos:
        print(Runner(repos, confirm=True).gen_build_and_run_commands(loc = 'local'))
    exit(0)
    Runner(repos, confirm=True).run_multiple_repos(loc = 'cantas_test', checkonly = False, port = '')
    print('Ne felejtsd el beírni ide: https://icellmobilsoft-int.atlassian.net/wiki/spaces/DAT/pages/46761949/Minden+amit+tudni+akart+l+az+mlff+t+blav+ltoz+sokr+l...')
