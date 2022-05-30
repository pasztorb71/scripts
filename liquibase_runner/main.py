import glob
import os

from Runner import Runner

def load_from_file(fname):
    with open(fname, 'r') as f:
        return f.read().split()

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    #repos = load_from_file('repos.txt')
    repos = ['mlff-enforcement-detection-image-postgredb']
    runner = Runner(base)
    #runner.kill('mlff-core-customer-postgredb')
    runner.run(repos, loc='local')
