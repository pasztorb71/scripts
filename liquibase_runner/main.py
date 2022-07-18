import os

from Runner import Runner

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    repos = os.listdir(base)
    repos = [x for x in repos if 'enforcement' in x]
    #repos = load_from_file('repos.txt')
    repos = ['mlff-core-notification-wa-postgredb']
    runner = Runner(base)
    #TODO beletenni maga előtt teljes törlés opciót
    runner.run(repos, loc='sandbox', full=False) #local ,sandbox, remote, dev, fit
