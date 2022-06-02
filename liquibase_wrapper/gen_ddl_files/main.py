def gen_files(project, owner, table, jira, version):
    filename = 'mlff-' + project + '-postredb'
    create_file(filename)


if __name__ == '__main__':
    base = ''
    gen_files(project='eobu-tariff',
              owner='bertalan.pasztor',
              table='road_network',
              jira='3231',
              version='0.4.0')