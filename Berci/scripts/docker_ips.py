base_ips = {'local':'gateway.docker.internal',
            'sandbox': 'gateway.docker.internal:5433',
            'dev': 'gateway.docker.internal:5434',
            'fit': 'gateway.docker.internal:5435',
            'perf': 'gateway.docker.internal:5436',
            'train': 'gateway.docker.internal:5437',
            'test': 'gateway.docker.internal:5438',
            'cron_test': 'gateway.docker.internal:5555'}

new_base = {'new_sandbox'   : 5440,
            'new_dev'       : 5540,
            'new_fit'       : 5640,
            'new_train'     : 5740,
            'new_test'     : 5740,
            'new_cantas_dev': 5840,
            }

offset = {'pg-doc': 0,
          'pg-core': 1,
          'pg-enforcement': 2,
          'pg-eobu': 3,
          'pg-payment': 4,
          'pg-settlement': 5,
          'pg-data': 6,
          }