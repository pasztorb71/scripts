import os
import subprocess


class Git:
    def __init__(self, base, repo):
        self.base = base
        self.repo = repo
        self.synced = ''

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