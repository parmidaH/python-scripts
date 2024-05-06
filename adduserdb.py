#import psycopg2
from signup import User
from psql import Database
#from pghelper import  PostgresHelper

class Adduser(User):
    
    def add_user(self, user: User):
        sql = "INSERT INTO public.users (first_name, last_name, phone_number, birth_date, sex, bio) VALUES (%s, %s, %s, %s, %s, %s)"
        self.cursor.execute(sql, (user.first_name, user.last_name, user.phone_number, user.birth_date, user.sex, user.bio))
        self.connection.commit()  # Add this line to commit the changes


# Create a new Database instance and connect to the database
db = Database(dbname='signup', user='signup', password='123456', host='localhost', port='5432')
#add user
adduser = Adduser()
adduser.add_user(User(first_name='parmida', last_name='heydari', phone_number='0989129494759', birth_date='1990-01-01', sex='female', bio='This is a test user'))

# Close the connection
db.close()
