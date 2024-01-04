import os
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime
from typing import List

import Repository

@dataclass
class Commit:
    sha: str
    author: str
    date: str
    message: str

@dataclass
class ListOfCommits:
    commitlist: List[Commit]

    @property
    def has_commits(self):
        return len(self.commitlist) > 0

    def commitlist_include(self, message):
        return any([message in c.message for c in self.commitlist])


class Git:
    def __init__(self, base: str='c:/GIT/MLFF/', repo: str=None):
        self.base = base
        self.repo = repo
        self.synced = ''

    def __repr__(self):
        return self.repo

    @classmethod
    def get_gitlist(cls, exclude=[]):
        repo = Repository.Repository()
        base = repo.get_base()
        repo_names = repo.get_repo_names_exclude(exclude)
        return [cls(base, name) for name in repo_names[0:]]

    @staticmethod
    def gen_clone_commands_for_all():
        gitlist = Git.get_gitlist()
        urls = [git.remote_url for git in gitlist]
        return 'git clone ' + '\ngit clone '.join(urls)

    def raw_commits_on_file_on_branch(self, file, branch='master'):
        if self.current_branch != branch:
            self.checkout_branch(branch)
        cmd = f' log --date=format:"%Y-%m-%d %H:%M:%S" -- {file}'
        p = subprocess.Popen('cmd /u /c git -C ' + self.base + '/' + self.repo + ' ' + cmd, stdout=subprocess.PIPE)
        result = p.communicate()
        text = result[0].decode('utf8')
        return text

    def commits_on_file_on_branch(self, file, after='2000-01-01 00:00:00', branch='master') -> ListOfCommits:
        list_of_commits = []
        l = ListOfCommits(list_of_commits)
        raw_commits = self.raw_commits_on_file_on_branch(file, branch)
        x = raw_commits.split('commit ', 1)[1]
        for commit in x.split('\n\ncommit '):
            arr = commit.splitlines()
            if 'Merge: ' in arr[1]:
                arr.pop(1)
            date = arr[2].replace('Date:   ', '')
            try:
                if datetime.strptime(date, "%Y-%m-%d %H:%M:%S") <= after:
                    continue
            except Exception as e:
                print(file)
                raise(e)
            c = Commit(sha=arr[0],
                       author=arr[1].replace('Author: ', ''),
                       date=date,
                       message=''.join([x for x in arr[3:] if x]).lstrip())
            l.commitlist.append(c)
        return l

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

    @property
    def current_branch(self):
        return os.popen('cmd /u /c git -C ' + self.base + '/' + self.repo + ' branch --show-current ').read().replace('\n','')

    @property
    def remote_url(self):
        return os.popen('cmd /u /c git -C ' + self.base + '/' + self.repo + ' config --get remote.origin.url ').read().replace('\n','')

    def checkout_branch(self, branch):
        self._run_command('checkout ' + branch, ['Already on', 'Switched to branch'])

    def new_branch(self, branch):
        self._run_command('checkout -b ' + branch, ['Switched to a new branch'])
        print(f'{branch} created.')

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

if __name__ == '__main__':
    print(Git.gen_clone_commands_for_all())
