import glob
import os

from Runner import Runner

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    repos = ['mlff-payment-transaction-postgredb']
    runner = Runner(base, 'fLXyFS0RpmIX9uxGII4N')
    runner.run(repos, loc='remote')
