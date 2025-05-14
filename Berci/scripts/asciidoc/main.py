"""A program előállítja <projektnév>_tables_attributes.adoc fájlt az adatbázisból"""
import click
from Database import Database

@click.command()
@click.option('--database_name', '-d', help='Database name', default='paibox_db')
@click.option('--port', '-p', help='port number', default=5432)
@click.option('--output_file', '-o', help='Output file name', default='tables_attributes.adoc')

def generate_adoc(database_name, port, output_file):
    db = Database(database_name, host='localhost', port=port)
    with open(output_file, 'w', encoding='utf8') as f:
        for table in db.tables.values():
            f.write(f'.{table.name}\n')
            f.write('|===\n')
            columns = table.get_structure()
            for column in columns:
                f.write(column[0] + '\n')
            f.write('|===' + '\n\n')

if __name__ == '__main__':
    generate_adoc()