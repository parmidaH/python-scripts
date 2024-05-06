from fastapi import FastAPI, HTTPException, Request, Body
from models import User
from adduserdb import Adduser
from datetime import date

app = FastAPI()
adduser = Adduser()

@app.post("/signup")
async def validate_user(request: Request, user: User = Body(...)):
    if not request.headers.get("content-type") == "application/json":
        raise HTTPException(status_code=415, detail="Unsupported Media Type. Use application/json")
    # today = date.today()
    # birth_date = date.fromisoformat(user.birth_date)
    # age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    # adduser.add_user(user)
    return {"message": "Validation successful"}


# @app.get("/age")
# async def calculate_age(user: User):
#     today = date.today()
#     birth_date = date.fromisoformat(user.birth_date)
#     age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
#     return {"age": age}


