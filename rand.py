import psycopg2
import datetime

# Connect to the database
conn = psycopg2.connect("dbname='signup' user='signup' host='localhost' password='123456'")
cur = conn.cursor()

# Check if the table exists
cur.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'users')")
exists = cur.fetchone()[0]

# Close the connection
cur.close()
conn.close()

# Print the result
print(exists)


