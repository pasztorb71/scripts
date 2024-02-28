import Environment
from Git.Git_class import Git
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


def get_remote_image_tags(repo):
    pass


if __name__ == '__main__':
    #repos = [Repository('customer')]
    loc = 'local'
    repos = [Repository(x) for x in Repository.get_repo_names() if '' in x][0:]
    print(Runner(repos, confirm=True).gen_run_commands(loc=loc, last_ver_from='nexus'))

