import json

t = """		"core": {
			"parent": "{env}"
		},
		"enforcement": {
			"parent": "{env}"
		},
		"payment": {
			"parent": "{env}"
		},
		"settlement": {
			"parent": "{env}"
		},
		"eobu": {
			"parent": "{env}"
		}"""
if __name__ == '__main__':
    file = 'c:/Users/bertalan.pasztor/AppData/Roaming/DBeaverData/workspace6/MLFF_altalanos/.dbeaver/data-sources.json1'
    l = ["CANTAS_TRAIN","CANTAS_DEV","CANTAS_TEST","CANTAS_PROD","icell_dev","icell_fit","icell_perf","icell_sandbox"]
    for i in l:
        print(t.replace('{env}', i),end='')
        print(',')