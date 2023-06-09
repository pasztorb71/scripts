base_ips = {'local':'gateway.docker.internal:5432',
            'perf': 'gateway.docker.internal:5436',
            'cron_test': 'gateway.docker.internal:5555'}

new_base = {'local'     : 5432,
            'sandbox'   : 5440,
            'dev'       : 5540,
            'fit'       : 5640,
            'train'     : 5740,
            'test'      : 5840,
            'perf'      : 5940,
            'c_dev'     : 6040,
            }

offset = {'pg-doc': 0,
          'pg-core': 1,
          'pg-enforcement': 2,
          'pg-eobu': 3,
          'pg-payment': 4,
          'pg-settlement': 5,
          'pg-data': 6,
          'pg-obu': 7,
          }

env_inst_end = {'sandbox'   : 'mqid',
                'dev'       : 'mskl',
                'fit'       : 'eldm',
                'train'     : '97nz',
                'test'      : 'oksl',
               }