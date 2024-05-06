import psycopg2
from psycopg2.extras import RealDictCursor

class Database():
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = psycopg2.connect(
            dbname=dbname, user=user, password=password, host=host, port=port
        )
        self.connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)
        print("Connected to the database")

    # def add_user(self, user: dict):
    #     sql = "INSERT INTO users (first_name, last_name, phone_number, birth_date, sex, bio) VALUES (%s, %s, %s, %s, %s, %s)"
    #     self.cursor.execute(sql, (user['first_name'], user['last_name'], user['phone_number'], user['birth_date'], user['sex'], user['bio']))
    #     self.connection.commit()  # Commit the changes

    def close(self):
        self.connection.close()

# Create a new Database instance and connect to the database
db = Database(dbname='signup', user='signup', password='123456', host='localhost', port='5432')

# Close the connection
#db.close()