hash_in_fk = """SELECT x.foreign_table, x.fk_column, xx.amname
from
(select kcu.table_schema || '.' || kcu.table_name as foreign_table,
       kcu.column_name as fk_column
from information_schema.table_constraints tco
join information_schema.key_column_usage kcu
          on tco.constraint_schema = kcu.constraint_schema
          and tco.constraint_name = kcu.constraint_name
join information_schema.referential_constraints rco
          on tco.constraint_schema = rco.constraint_schema
          and tco.constraint_name = rco.constraint_name
join information_schema.key_column_usage rel_kcu
          on rco.unique_constraint_schema = rel_kcu.constraint_schema
          and rco.unique_constraint_name = rel_kcu.constraint_name
          and kcu.ordinal_position = rel_kcu.ordinal_position
where tco.constraint_type = 'FOREIGN KEY'
order by kcu.table_schema,
         kcu.table_name,
         kcu.ordinal_position
) x
join       
(
SELECT distinct ns.nspname||'.'||tab.relname AS tabname, am.amname
FROM pg_index idx 
JOIN pg_class cls ON cls.oid=idx.indexrelid
JOIN pg_class tab ON tab.oid=idx.indrelid
JOIN pg_am am ON am.oid=cls.relam
JOIN pg_catalog.pg_namespace AS ns ON tab.relnamespace = ns.oid
WHERE cls.relname LIKE 'pk_%'
) xx
ON x.foreign_table = xx.tabname
WHERE amname != 'btree'"""