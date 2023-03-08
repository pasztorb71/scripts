import os


def get_csapatok():
    with open('c:/Users/bertalan.pasztor/PycharmProjects/liquibase/Berci/scripts/csapatok.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    csapatok = get_csapatok()
    dirs = os.listdir('c:/GIT/MLFF/')
    cs = [x.split(' ',1)[0] for x in csapatok.split('\n') if x]
    print('dir-csapatok')
    print(set(dirs) - set(cs))
    print('csapatok-dirs')
    print(set(cs) - set(dirs))
