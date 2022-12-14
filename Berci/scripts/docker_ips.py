base_ips = {'local':'gateway.docker.internal',
            'sandbox': 'gateway.docker.internal:5433',
            'dev': 'gateway.docker.internal:5434',
            'fit': 'gateway.docker.internal:5435',
            'perf': 'gateway.docker.internal:5436',
            'train': 'gateway.docker.internal:5437',
            'cron_test': 'gateway.docker.internal:5555'}

new_base = {'new_sandbox'   : 5440,
            'new_dev'       : 5540,
            'new_fit'       : 5640,
            'new_train'     : 5740,
            'new_cantas_dev': 5840,
            }

offset = {'pg-doc-mqid': 0,
          'pg-core-mqid': 1,
          'pg-enforcement-mqid': 2,
          'pg-eobu-mqid': 3,
          'pg-payment-mqid': 4,
          'pg-settlement-mqid': 5,
          'pg-data-mqid': 6,
          }