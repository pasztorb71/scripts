import glob
import os

from Runner import Runner

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    repos = ['mlff-enforcement-detection-decision-postgredb']
    runner = Runner(base)
    #runner.kill('mlff-core-customer-postgredb')
    runner.run(repos, loc='local')
