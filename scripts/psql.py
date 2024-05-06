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

    def close(self):
        self.connection.close()


db = Database( dbname="signup", user="signup", password="123456", host="localhost", port="5432")