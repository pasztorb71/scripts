

def choose_project(reponame=None):
    if reponame in ('trino', 'backend', 'meta', 'parser'):
        return 'AKP'
    elif reponame in ('emap'):
        return 'BC'
    x = 3
    out = ''
    d = {
        '1': 'MLFFSUP',
        '2': 'PEKTRMSS',
        '3': 'LZL',
        '4': 'BC',
        '5': 'AKP',
    }
    while x not in ['1', '2', '3', '4', '5']:
        x = input('Válassz projektet:\n'
                  '1: MLFFSUP\n'
                  '2: PEKTRMSS\n'
                  '3: LZL\n'
                  '4: EMAP\n'
                  '5: AKP\n'
        )
    return d[x]


def base_from_project(proj):
    d = {'MLFFSUP': 'c:/GIT/MLFF/',
         'PEKTRMSS': 'c:/GIT/MLFF/',
         'LZL': 'c:/GIT/ELAZLAP/',
         'BC': 'C:/GIT/EMAP/',
         'AKP': 'c:/GIT/AKP/',
         }
    return d[proj]
