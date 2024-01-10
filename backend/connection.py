import psycopg2
import config.config as config
def create_table():
    # Connect to the PostgreSQL database
    print ("Connecting to PostgreSQL database", config.host, config.port)
    conn = psycopg2.connect(
         host="localhost",
        port="5432",
        user="user",
        password="user",
        database="certificate"
    )

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Define the SQL statement to create the table
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS certificate (
            id  SERIAL PRIMARY KEY,
            firstName VARCHAR(100),
            middleName VARCHAR(100),
            lastName VARCHAR(100),
            certificate VARCHAR(250)
            
        )
    '''

    # Execute the SQL statement to create the table
    cursor.execute(create_table_query)

    # Commit the transaction and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()