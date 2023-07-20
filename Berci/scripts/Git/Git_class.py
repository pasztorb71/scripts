import os
import subprocess
import Repository


class Git:
    @staticmethod
    def get_gitlist():
        repo = Repository.Repository()
        base = repo.get_base()
        repo_names = repo.get_repo_names()
        return [Git(base, name) for name in repo_names[0:]]

    @staticmethod
    def gen_clone_commands_for_all():
        gitlist = Git.get_gitlist()
        urls = [git.get_remote_url() for git in gitlist]
        return 'git clone ' + '\ngit clone '.join(urls)

    def __init__(self, base=None, repo=None):
        self.base = base
        self.repo = repo
        self.synced = ''

    def __repr__(self):
        return self.repo

    def print_log(self):
        os.system('git -C ' + self.repo + ' log --oneline')

    def diff(self, src, dest):
        os.system('git -C ' + self.repo + ' fetch origin master')
        os.system('git -C ' + self.repo + ' checkout master')

    def is_master_synced(self, branch='master'):
        os.popen('git -C ' + self.base + '/' + self.repo + ' fetch --all --prune')
        proc = subprocess.Popen('cmd /u /c git -C ' + self.base + '/' + self.repo + ' diff ' + branch + ' origin/' + branch,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        res = proc.stdout.read()
        if res == b'':
            self.synced = True
        else:
            self.synced = False
        return self.synced

    def get_current_branch(self):
        return os.popen('cmd /u /c git -C ' + self.base + '/' + self.repo + ' branch --show-current ').read().replace('\n','')

    def get_remote_url(self):
        return os.popen('cmd /u /c git -C ' + self.base + '/' + self.repo + ' config --get remote.origin.url ').read().replace('\n','')

    def checkout_branch(self, branch):
        self._run_command('checkout ' + branch, ['Already on', 'Switched to branch'])

    def new_branch(self, branch):
        self._run_command('checkout -b ' + branch, ['Switched to a new branch'])

    def _run_command(self, cmd, acceptable_err):
        proc = subprocess.Popen('cmd /u /c git -C ' + self.base + '/' + self.repo + ' ' + cmd,
                                stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        stdout, stderr = proc.communicate()
        if stderr and not any([x in stderr for x in acceptable_err]):
            raise Exception(stderr)

    def init(self):
        os.system(f'git -C {self.base}/{self.repo} restore --staged etc/release/release.sh')
        os.system(f'git -C {self.base}/{self.repo} restore .')
        os.system(f'git -C {self.base}/{self.repo} clean -f -d')


def git_init_from_path(path):
    a = path.split('\\', 2)
    repo = a[0] + '/' + a[1]
    g = Git(repo)
    g.init()