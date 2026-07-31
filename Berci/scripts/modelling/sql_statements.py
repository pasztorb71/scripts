table_names_related_to_table = """
SELECT 
    tc.table_schema, 
    tc.table_name, 
    kcu.column_name 
FROM 
    information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
WHERE 
    tc.constraint_type = 'FOREIGN KEY' AND
    ccu.table_name = %(table_name)s AND
    ccu.table_schema = %(table_schema)s AND
    tc.table_schema = %(table_schema)s
UNION ALL
-- select all tables that referenced by akp_masterdata.station table
SELECT 
    ccu.table_schema AS foreign_table_schema,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name
FROM 
    information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name     
WHERE 
    tc.constraint_type = 'FOREIGN KEY' AND
    tc.table_name = %(table_name)s AND
    tc.table_schema = %(table_schema)s AND 
	ccu.table_schema = %(table_schema)s
"""