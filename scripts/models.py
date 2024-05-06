from pydantic import BaseModel, Field, validator

class User(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    birth_date: str
    sex: str
    bio: str
    age: int = Field(None, alias="age", description="The age of the user", required=False)


    @validator('first_name', 'last_name')
    def name_must_be_valid(cls, v):
        if not v.isalpha():
            raise ValueError("Names must contain only alphabetic characters")
        if len(v) < 3:
            raise ValueError('Names must be at least 3 characters long')
        return v

    @validator('phone_number')
    def phone_number_must_be_valid(cls, v):
        if not v.isdigit():
            raise ValueError('Phone number must contain only digits')
        if len(v) != 13:
            raise ValueError('Phone number must be 13 digits long')
        return v

    @validator('birth_date')
    def birth_date_must_be_valid(cls, v):
        if len(v) != 10:
            raise ValueError('Birth date must be in the format YYYY-MM-DD')
        return v

    @validator('sex')
    def sex_must_be_valid(cls, v):
        if v.lower() not in ['male', 'female']:
            raise ValueError('Sex must be one of "male", "female"')
        return v

    @validator('bio')
    def bio_must_be_valid(cls, v):
        if len(v) < 10:
            raise ValueError('Bio must be at least 10 characters long')
        return v
    
    