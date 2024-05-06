import psycopg2
from psycopg2 import OperationalError
from threading import Lock


class PostgresHelper:
    _lock = Lock()

    def __init__(self):
        self.config = {
            "dbname": "signup",
            "user": "signup",
            "password": "123456",
            "host": "localhost",
            "port": "5432"
        }
        self._connection = None
        self._connect()

    def _connect(self):
        try:
            self._connection = psycopg2.connect(**self.config)
            self._connection.autocommit = True
            print("connected")
        except OperationalError as e:
            print("Error connecting to the database:", e)

    def execute_query(self, query):
        try:
            if self._connection is None:
                self._connect()

            with self._connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                return result
        except OperationalError as e:
            # Attempt to reconnect and retry the query
            print("Reconnecting and retrying query:", e)
            self._connect()
            return self.execute_query(query)
        
# Create an instance of the PostgresHelper class
postgres_helper = PostgresHelper()

# Execute a query
query_result = postgres_helper.execute_query("SELECT * FROM users;")
print(query_result)        