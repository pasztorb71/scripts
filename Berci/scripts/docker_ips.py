base_ips = {'local':['gateway.docker.internal'],
            'sandbox': ['gateway.docker.internal:5433'],
            'dev': ['gateway.docker.internal:5434'],
            'fit': ['gateway.docker.internal:5435'],
            'perf': ['gateway.docker.internal:5436']}

ipdict = {'remote': base_ips['sandbox'] + base_ips['dev'],
          'all': base_ips['sandbox'] + base_ips['dev'] + base_ips['fit']
          }
