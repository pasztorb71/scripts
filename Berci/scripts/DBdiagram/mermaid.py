from Database import Database

if __name__ == '__main__':
  d = {}
  db = Database('eobu_tariff')
  for tab in db.tables.values():
      tab.fill_foreign_keys()
      fks = tab.foreign_keys
      if fks:
          d[tab.name] = []
          for fk in fks.values():
              d[tab.name].append(fk.ref_table)
  print("""digraph G { 
  rankdir = TB;
  subgraph {""")
  for parent, children in d.items():
      for child in children:
          print(f'    {child} -> {parent}')
  print("""  } /* closing subgraph */
}""")