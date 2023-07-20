import Repository
from Git.Git_class import Git
from Git.utils_parallel_runner import parallel_run, _mproc_multiple_commands


def get_all_tags(gitlist):
    commands = ['tag -l']
    ret_dict = parallel_run(gitlist, _mproc_multiple_commands, commands)
    return ret_dict


def is_item_nedeed(item):
    return \
        'postgredb-0.16.1' in item[1]['stdout'][0] and \
        'postgredb-0.17.' in item[1]['stdout'][0]


def print_ret_dict_to_file(folder, ret_dict):
    for item in ret_dict.items():
        if not is_item_nedeed(item):
            continue
        with open(folder+item[0], 'w') as f:
            f.write(item[1]['stdout'][0])

if __name__ == '__main__':
    folder = 'c:/Users/bertalan.pasztor/Documents/MLFF/PYTHON_OUT/tags/'
    gitlist = Git.get_gitlist()[0:]
    ret_dict = get_all_tags(gitlist)
    print_ret_dict_to_file(folder, ret_dict)
