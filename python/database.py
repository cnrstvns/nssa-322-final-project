import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

# Get the environment variables for the database connection
db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

def create_connection():
    # Create a MySQL connection
    try:
        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        return conn

    except mysql.connector.Error as e:
        print(f'Error connecting to the MySQL database: {e}')
        return e
    
if __name__ == '__main__':
    conn = create_connection()
    print('Successfully connected to the MySQL database!')

    query = "SELECT now()"
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchone()
    print('Result of query:', results)

    # Close the MySQL connection
    conn.close()
    print('Connection to the MySQL database closed.')