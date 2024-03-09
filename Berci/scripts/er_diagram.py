import psycopg2
import pygraphviz as pgv

def get_table_names(cursor):
    """Get the names of all tables in the database."""
    cursor.execute(
        "SELECT table_name FROM information_schema.tables WHERE table_schema = 'tariff' and table_name not like '%$hist%'"
    )
    return [row[0] for row in cursor.fetchall()]

def get_foreign_keys(cursor, table_name):
    """Get foreign keys for a given table."""
    cursor.execute(
        f"""
        SELECT
            tc.table_name, kcu.column_name, ccu.table_name AS foreign_table_name, 
            ccu.column_name AS foreign_column_name
        FROM 
            information_schema.table_constraints AS tc 
            JOIN information_schema.key_column_usage AS kcu
              ON tc.constraint_name = kcu.constraint_name
            JOIN information_schema.constraint_column_usage AS ccu
              ON ccu.constraint_name = tc.constraint_name
        WHERE 
            constraint_type = 'FOREIGN KEY' AND tc.table_name='{table_name}'
        """
    )
    return cursor.fetchall()

def create_er_diagram(table_names, foreign_keys):
    """Create an ER diagram using Graphviz."""
    graph = pgv.AGraph(strict=True, directed=True)

    # Add nodes for tables
    for table_name in table_names:
        graph.add_node(table_name, shape='box')

    # Add edges for foreign keys
    for fk in foreign_keys:
        graph.add_edge(
            fk[0], fk[2], label=f"{fk[1]} -> {fk[3]}", arrowhead='vee'
        )

    return graph

def main():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        "dbname='eobu_tariff' user='postgres' host='localhost' password='postgres'"
    )
    cursor = conn.cursor()

    # Get table names and foreign keys
    table_names = get_table_names(cursor)
    foreign_keys = []
    for table_name in table_names:
        foreign_keys.extend(get_foreign_keys(cursor, table_name))

    # Create ER diagram
    er_diagram = create_er_diagram(table_names, foreign_keys)

    # Save ER diagram as an image file
    er_diagram.draw('er_diagram.png', prog='dot')
    print("ER diagram saved as er_diagram.png")

    # Close database connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()
