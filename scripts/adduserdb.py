from models import User
from psql import Database

class Adduser():
    def __init__(self):
        self.db = Database(dbname='signup', user='signup', password='123456', host='localhost', port='5432')

    def add_user(self, user: User):
        sql = """
        INSERT INTO users (first_name, last_name, phone_number, age, birth_date, sex, bio) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        #self.db.cursor.execute(sql,(user.first_name, user.last_name, user.phone_number, calculate_age((age), user.birth_date, user.sex, user.bio))
        #self.db.cursor.execute(sql,(user.first_name, user.last_name, user.phone_number, user.age, user.birth_date, user.sex, user.bio))
        
        self.db.connection.commit()  # Commit the changes



# Create a new Database instance and connect to the database
#db = Database(dbname='signup', user='signup', password='123456', host='localhost', port='5432')
#add user
adduser = Adduser()
adduser.add_user(User(first_name='parmida', last_name='heydari', phone_number='0989129494759', birth_date='1990-01-01', sex='female', bio='This is a test user'))

# Close the connection
#Database.db.close()