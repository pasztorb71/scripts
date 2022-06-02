
from Runner import Runner

def load_from_file(fname):
    with open(fname, 'r') as f:
        return f.read().split()

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    #repos = load_from_file('repos.txt')
    repos = ['mlff-eobu-tariff-postgredb']
    runner = Runner(base)
    runner.run(repos, loc='sandbox')
