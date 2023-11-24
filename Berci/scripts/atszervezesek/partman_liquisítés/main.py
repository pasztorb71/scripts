import os

from atszervezesek.partman_liquisítés.templates import incl_template, install_template, sqlfile_template, \
    template_1, template_2

WORKDIR = 'c:/GIT/pg_partman_custom/sql/'

if __name__ == '__main__':
    includes = []
    dirnames = ['types', 'tables']
    for dirname in dirnames:
        files = [f for f in os.listdir(WORKDIR+dirname) if f.endswith('.sql')]
        for file in files:
            with open(WORKDIR+file.replace('.sql', '.xml'), 'w') as f:
                f.write(template_1.replace('{name}', file.replace('.sql','')).replace('{dir}', dirname))
            includes.append(incl_template.
                            replace('{dirname}', dirname).
                            replace('{name}', file.replace('.sql', '')))

    dirnames = ['functions', 'procedures']
    for dirname in dirnames:
        incls = []
        includes.append(incl_template.replace('{name}', dirname).replace('.sql', ''))
        files = [f for f in os.listdir(WORKDIR+dirname) if f.endswith('.sql')]
        for file in files:
            incls.append(sqlfile_template.replace('{name}', file).replace('{dir}', dirname))
        with open(WORKDIR+dirname+'.xml', 'w') as f:
            f.write(template_2
                    .replace('{sqlfile_template}', '\n\t\t'.join(incls))
                    .replace('{name}', dirname))

    incl = '\n'.join(includes)
    install_template = install_template.replace('{incl_template}', incl)
    with open(WORKDIR+'liquibase-install-partman.xml', 'w') as f:
        f.write(install_template)
