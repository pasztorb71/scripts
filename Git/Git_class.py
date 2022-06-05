import os


class Git:
    def __init__(self, repo):
        self.repo = repo

    def print_log(self):
        os.system('git -C ' + self.repo + ' log --oneline')

    def diff(self, src, dest):
        os.system('git -C ' + self.repo + ' fetch origin master')
        os.system('git -C ' + self.repo + ' checkout master')
