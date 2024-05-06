from fastapi import FastAPI, HTTPException, Request, Body
from datetime import date
from pydantic import BaseModel, validator
from psql import Database
from adduserdb import Adduser

#import re

app = FastAPI()
#db = Database(dbname='signup', user='signup', password='123456', host='localhost', port='5432')
#adduser = Adduser()

class User(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    #age: str
    birth_date: str
    sex: str
    bio: str

    @validator('first_name', 'last_name')
    def name_must_be_valid(cls, v):
        if not all(char.isalpha() for char in v):
            raise ValueError("cannot contain non alphabetic characters")
        # if not re.match(r'^[a-zA-Z]+$', v):
        #     raise ValueError('must contain only alphabetic characters')
        if len(v) < 3:
            raise ValueError('must be at least 3 characters long')
        return v
    
    
    @validator('phone_number')
    def phone_number_must_be_valid(cls, v):
        if not all(char.isdigit() for char in v):
            raise ValueError('Phone number must contain only digits')
        if len(v) != 13:  
            raise ValueError('Phone number must be 13 digits long')
        return v

    # @validator('age')
    # def age_must_be_valid(cls, v):
    #     if not all(char.isdigit() for char in v):
    #         raise ValueError('Age must contain only digits')
    #     if len(v) != 2:  
    #         raise ValueError('Age must be 2 digits long')
    #     return v
    
    @validator('birth_date')
    def birth_date_must_be_valid(cls, v):
        if not isinstance(v, str):
            raise ValueError('must be a string')
        if len(v) != 10:
            raise ValueError('must be at least 10 characters long')
        return v
        
    @validator('sex')
    def sex_must_be_valid(cls, v):
        if not isinstance(v, str):
            raise ValueError('Sex must be a string')
        if v.lower() not in ['male', 'female']:
            raise ValueError('Sex must be one of "male", "female"')
        return v

    @validator('bio')
    def bio_must_be_valid(cls, v):
        if not isinstance(v, str):
            raise ValueError('must be a string')
        return v

@app.post("/signup")
async def validate_user(request: Request, user: User = Body(...)):
    if not request.headers.get("content-type") == "application/json":
        raise HTTPException(status_code=415, detail="Unsupported Media Type. Use application/json")
    #adduser.add_user(user)
    return {"message": "Validation successful"}



@app.get("/age")
async def calculate_age(user: User):
    today = date.today()
    birth_date = date.fromisoformat(user.birth_date)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return {"age": age}



