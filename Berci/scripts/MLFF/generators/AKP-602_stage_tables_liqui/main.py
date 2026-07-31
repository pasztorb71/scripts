import os
import shutil

import click

def create_seq_generator(start):
    i = start
    while True:
        i += 1
        yield i

def get_first_table_pos(lines) -> int:
    for i, line in enumerate(lines):
        if line.startswith('CREATE TABLE'):
            return i

def get_table_blocks_from_file(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
    table_blocks = dict()
    table_name = ''
    pos = get_first_table_pos(lines)
    for line in lines[pos:]:
        if line.startswith('CREATE TABLE'):
            line = line.replace('lakehouse.prototype_consolidated','${schema_name}')
            if 'table_block' in locals():
                table_blocks[table_name] = table_block
            table_block = list()
            table_name = line.rsplit('.',1)[1].split(' ')[0]
            print(table_name)
        table_block.append(line)
    table_blocks[table_name] = table_block
    return table_blocks

def gen_changeset(tablename, table_ddl, seqnum, ticket):
    ddl = ''.join(table_ddl)
    return f"""--liquibase formatted sql

--changeset bertalan.pasztor:{seqnum}
--comment {ticket} {tablename} tábla_létrehozása

{ddl}
"""

@click.command()
@click.option(
    "--seq_start",
    help="Fájl sorszám kezdő", default=16)
@click.option(
    "--infile",
    help="input file with tables", default="stage_tablak.sql")
@click.option(
    "--schemaname",
    help="Schema name", default="prototype_consolidated")
@click.option(
    "--ticket",
    help="ticket", default="AKP-602")
def main(seq_start, infile, schemaname, ticket):
    """
    :param outfile: Output fájl
    """
    seq_generator = create_seq_generator(start=seq_start)
    table_blocks = get_table_blocks_from_file(infile)
    drop_commands = ''
    shutil.copy('sample/schema-version-0.1.0.xml', 'schema-version-0.1.0.xml')
    for tablename, schema in table_blocks.items():
        tabdir = f'tables/{tablename}'
        if not os.path.exists(tabdir):
            os.mkdir(tabdir)
        table_ddl = schema
        next_seq = next(seq_generator)
        file_seq_num = str(next_seq).rjust(4, '0')
        changeset = gen_changeset(tablename, table_ddl, file_seq_num, ticket)
        with open(f'{tabdir}/{file_seq_num}-{tablename}-create.sql', 'w', encoding='utf8') as f:
            f.write(changeset)
        with open(f'schema-version-0.1.0.xml', 'r', encoding='utf8') as f:
            versions = f.readlines()
        with open(f'schema-version-0.1.0.xml', 'w', encoding='utf8') as f:
            out = ''.join(versions[:-2])
            out += f'    <include file="../tables/{tablename}/{file_seq_num}-{tablename}-create.sql" relativeToChangelogFile="true"/>\n'
            out += ''.join(versions[-2:])
            f.write(out)
        drop_commands += f'DROP TABLE IF EXISTS lakehouse.{schemaname}.{tablename};\n'
        with open(f'drop-all-tables.sql', 'w', encoding='utf8') as f:
            f.write(drop_commands)


if __name__ == '__main__':
    main()