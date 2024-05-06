
from datetime import date
def calculate_age(born):
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    #true 1, false 0
    #((today.month, today.day) < (born.month, born.day)) --> bool
    #print((today.month, today.day)) 
    #print(((born.month, born.day)))
    #print(((today.month, today.day) < (born.month, born.day)))
    return age
birth_date = date(1990, 7, 1)
age = calculate_age(birth_date)
print(age)
                                                                                                                                            