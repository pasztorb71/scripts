import os


class Repository():
    def __init__(self, name=''):
        self.root = 'c:/GIT/MLFF/'
        self.name = self.get_name(name)
        

    def get_base(self):
        return 'c:/GIT/MLFF/' + self.name + '/liquibase/'

    def get_name(self, name):
        repos = os.listdir(self.root)
        a = [repo for repo in repos if name in repo]
        if len(a) > 1:
            print(a)
            raise Exception("Nem egyértelmű a repository név!")
        return a[0]