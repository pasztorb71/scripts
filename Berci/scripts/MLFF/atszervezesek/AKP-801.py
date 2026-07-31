import glob
import os
from pprint import pprint

base_path = r'c:\GIT\AKP\data-lakehouse-trino-liquibase\liquibase'
file_pattern =  '*-create.sql'
#file_pattern =  '*0034-error_summary-create.sql'
#file_pattern =  '*0020-stage_xtx_lane_configuration_header-create.sql'
pattern = os.path.join(base_path, '**', file_pattern)

for file_path in glob.glob(pattern, recursive=True):
    with (open(file_path, 'r', encoding='utf-8') as file):
        try:
            content = file.read().replace('timestamp(6)', 'timestamp')
            content= content.splitlines()
            index = [i for i, line in enumerate(content) if ')' in line][0]
            content[index-1] += ','
            if '\\landing\\' in file_path:
                content.insert(index, '  line_number varchar')
            else:
                content.insert(index, '  line_number integer')
            print('\n'.join(content))
        except Exception as e:
            print(f"Error processing file {file_path}: {e}")
            print('\n'.join(content))
            raise e
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('\n'.join(content))


