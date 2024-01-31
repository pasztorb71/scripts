import os
import shutil
from distutils.dir_util import copy_tree

from utils import utils


def append_to_file_after_line_last_occurence(fname, after, what):
  with open(fname, 'r', encoding='utf-8') as f:
    text = f.readlines()
  already_exists = [idx for idx, s in enumerate(text) if what in s]
  if already_exists:
    return
  index_after = utils.get_last_nth_occurence_of_list_element(text, after, 1)
  if not index_after:
      index_header_end = utils.get_last_nth_occurence_of_list_element(text, '    <!-- ==================================', 1)
      if not index_header_end:
        return
      else:
          index_after = index_header_end + 1
  text.insert(index_after, what + '\n')
  with open(fname, 'w', encoding='utf-8') as out:
    out.write(''.join(text))


def copy_dir(src, dst, delete_dir_if_exists=False):
    print('dir : '+src, dst)
    if delete_dir_if_exists == False and os.path.isdir(dst):
        raise Exception('Directory már létezik: ' + dst)
    if os.path.isdir(src):
        print('  '+dst)
        copy_tree(src, dst)


def create_old_file(fname):
    if os.path.isfile(fname + '_old'):
        raise Exception('már létezik: ' + fname + '_old')
        # os.remove(fname)
        # move_file(fname + '_old', fname)
    move_file(fname, fname + '_old')

def replace_in_file(fname, from_to):
    text = ''
    with open(fname, 'r', encoding='utf-8',newline='') as f:
        text = f.read()
        for pair in from_to:
            text = text.replace(pair[0], pair[1])
            text = text.replace(pair[0].upper(), pair[1].upper())
    with open(fname, 'w', encoding='utf-8',newline='') as f:
        f.write(text)

def move_file(src, dst):
    print('file: '+src, dst)
    if os.path.isfile(src):
        print('  '+src)
        shutil.move(src, dst)

def copy_file(src, dst):
    print('file: '+src, dst)
    if os.path.isfile(src):
        print('  '+src)
        shutil.copyfile(src, dst)
    else:
        print('  '+ src + '  nem létezik')


def copy_file_and_replace(src, dst, from_to):
    copy_file(src, dst)
    replace_in_file(dst, from_to)


def move_dir(src, dst):
    print('dir : '+src, dst)
    if os.path.isdir(src):
        print('  '+src)
        shutil.move(src, dst)

def get_files_from_path_ext_and_cont_filtered(path, ext, cont):
    out = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext) and cont in file:
                out.append(os.path.join(root, file))
    return out


def get_files_from_path_fname_filtered(path, name):
    out = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if name in file:
                out.append(os.path.join(root, file))
    return out

def get_files_from_path_ext_filtered(path, ext):
    out = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                out.append(os.path.join(root, file))
    return out


def get_files_from_path_ext_find_content(path, ext, cont):
    out = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                if file_contains(os.path.join(root, file), cont):
                    out.append(os.path.join(root, file))
    return out

def file_contains(file, cont,):
    with open(file, 'r', encoding='utf-8') as f:
        if cont in f.read():
            return True
    return False

def load_from_file(fname):
    project_root = os.path.dirname(os.path.dirname(__file__))
    with open('/'.join([project_root,'scripts',fname]), 'r') as f:
        return [x for x in f.read().split('\n') if not x.startswith('#')]

def get_line_from_file_by_linepart(fname:str, linepart:str) -> str:
    with open(fname, 'r') as f:
        for l in f.readlines():
            if linepart in l:
                return l
    return None


def check_window_eol_in_sh_files():
    windows_eol = '\r\n'
    print('check_window_eol_in_sh_files:', end='')
    exceptions = []
    for file in get_files_from_path_fname_filtered('c:/GIT/MLFF/', '.sh'):
        with open(file, 'r') as f:
            c = f.readline()
            if f.newlines == windows_eol:
                exceptions.append(file)
    if exceptions:
        print('\n\t'+ '\n\t'.join(exceptions))
    else:
        print(' OK')

def del_file_ignore_error(path):
    try:
      os.remove(path)
    except OSError:
      pass