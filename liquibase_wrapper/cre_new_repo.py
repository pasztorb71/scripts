base_path = 'c:/GIT/MLFF/'
src_repo = 'core-postgredb'
dest_repo = 'mlff-payment-retry-postgredb'

def create_dest_file(old_name, new_name, replace_matrix):
    with open(old_name, 'r', encoding='utf-8') as oldf:
        with open(new_name, 'w', encoding='utf-8') as newf:
            for line in oldf:
                newline = line.replace(repl_from, repl_to).replace(repl_from.upper(), repl_to.upper())
                newf.write(newline)

def copy_readme():
    create_dest_file(src_repo+)


copy_readme()