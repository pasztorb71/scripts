import os

from atszervezesek.partman_liquisítés.templates import template, incl_template, install_template

WORKDIR = 'c:/GIT/pg_partman_custom/sql/'

if __name__ == '__main__':
    includes = []
    dirnames = ['types', 'tables', 'functions', 'procedures']
    for dirname in dirnames:
        files = [f for f in os.listdir(WORKDIR+dirname) if f.endswith('.sql')]
        for file in files:
            with open(WORKDIR+'xmls/'+file.replace('.sql', '.xml'), 'w') as f:
                f.write(template.replace('{name}', file).replace('{dir}', dirname))
            includes.append(incl_template.
                            replace('{dirname}', dirname).
                            replace('{name}', file.replace('.sql', '')))

    incl = '\n'.join(includes)
    install_template = install_template.replace('{incl_template}', incl)
    with open(WORKDIR+'liquibase-install-partman.xml', 'w') as f:
        f.write(install_template)
