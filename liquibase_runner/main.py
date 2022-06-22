from Runner import Runner

if __name__ == '__main__':
    base = 'c:/GIT/MLFF/'
    #repos = os.listdir(base)
    #repos = load_from_file('repos.txt')
    repos = ['mlff-eobu-trip-postgredb']
    runner = Runner(base)
    runner.run(repos, loc='sandbox') #local ,sandbox, remote, dev, fit
