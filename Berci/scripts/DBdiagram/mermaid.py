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
              if fk.ref_table not in d[tab.name]:
                d[tab.name].append(fk.ref_table)
  print("graph TD;", end='')
  for parent, children in d.items():
      for child in children:
          print(f'\n  {parent}-->{child};', end='')
