from graphviz2drawio import graphviz2drawio

from classes.Database import Database


def gen_dependencies(db):
    d = {}
    for tab in db.tables.values():
        tab.fill_foreign_keys()
        fks = tab.foreign_keys
        if fks:
            d[tab.name] = []
            for fk in fks.values():
                if fk.ref_table not in d[tab.name]:
                    d[tab.name].append(fk.ref_table)
    return d


def print_mermaid(d):
    print("graph TD;", end='')
    for parent, children in d.items():
        for child in children:
            print(f'\n  {parent}-->{child};', end='')

def write2file_graphviz(d, fname):
    with open(f'{fname}.dot', 'w') as f:
        f.write("""digraph G { 
  splines=false;
  node [shape="box"];
  rankdir = TB;
  subgraph {""")
        for parent, children in d.items():
            for child in children:
                f.write(f'\n    {child} -> {parent}')
        f.write("""
  } /* closing subgraph */
}""")
    print(f'dot -Tpng {fname}.dot -o {fname}.png')


def graphviz_to_drawio(dot_file_name):
    xml = graphviz2drawio.convert(f'{dot_file_name}.dot')
    with open(f'{dot_file_name}.drawio', 'w') as f:
        f.write(xml)


if __name__ == '__main__':
  path = 'c:/Users/bertalan.pasztor/Documents/drawio_diagrams/graphviz/'
  dbname = 'eobu_tariff'
  db = Database(dbname)
  d = gen_dependencies(db)
  print_mermaid(d)
  #write2file_graphviz(d, path+dbname)
  #graphviz_to_drawio(path+dbname)


