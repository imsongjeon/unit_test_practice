import psycopg2

def get_all_rows_from_table(db_credentials, table_name):
    allowed_table_names = ['test_table', 'another_table']
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(**db_credentials)
        # Create a new cursor
        cur = conn.cursor()
        # Execute the query
        if '.' in table_name:
            table_name = table_name.split('.')[-1]
        if table_name not in allowed_table_names:
            raise psycopg2.errors.ProgrammingError('Invalid table name')
        cur.execute('SELECT * FROM %s', (table_name,))
        # Fetch all rows from the query result
        rows = cur.fetchall()
        # Close the cursor and the connection
        cur.close()
        conn.close()
        # Return the fetched rows
        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")
        # Return None if an exception occurs
        return None