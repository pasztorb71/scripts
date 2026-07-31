import yaml
employee_dict={'5432__core_genos': [['genos', 'template_part_content', 'postgres'], ['genos', 'template_part', 'postgres']]}
print("The python dictionary is:")
print(employee_dict)
yaml_string=yaml.dump(employee_dict, )#.replace('- !!python/tuple\n','')
print("The YAML string is:")
print(yaml_string)