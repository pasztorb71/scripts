from Git_class import Git

if __name__ == '__main__':
    g = Git('c:/GIT/MLFF/mlff-eobu-tariff-postgredb/')
    g.diff('master', 'origin/master')