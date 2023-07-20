import os

from Git.Git_class import Git

path = 'c:\GIT\\teszt'
#os.system(f'rmdir /s /q {path}')
#os.system(f'mkdir {path}')
g = Git(path)
g.init()
