import psycopg2
from psycopg2 import sql

# Database connection parameters
db_params = {
    "dbname": "signup",
    "user": "signup",
    "password": "123456",
    "host": "localhost",
    "port": "5432",
}

def create_signup_table():
    try:
        # Connect to the PostgreSQL database
        connection = psycopg2.connect(**db_params)
        cursor = connection.cursor()

        # Create the 'users' table if not exists
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(100),
                last_name VARCHAR(100),
                phone_number VARCHAR(20),
                age INTEGER,
                birth_date DATE,
                sex VARCHAR(8),
                bio TEXT
            )
        """)

        # Commit changes and close the cursor and connection
        connection.commit()
        cursor.close()
        connection.close()

        print("Table created successfully.")

    except (Exception, psycopg2.Error) as error:
        print("Error creating table:", error)

if __name__ == "__main__":
    create_signup_table()