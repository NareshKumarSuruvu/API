from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field,EmailStr,ValidationError

app = FastAPI()

userlist=[]

class UserDetails(BaseModel):
    username:str = Field(min_length=3)
    email:EmailStr
    password:str = Field(min_length=8)

@app.post("/register")
def userRegistration(details:UserDetails):
    for u in userlist:
        if(u['username'] == details.username):
            raise HTTPException(status_code=400,detail='username is already exist')
    
    userlist.append(details.model_dump())
    print(userlist)
    return "User Added Suucessfully"

@app.get("/getusers")
def getUsers():
    return userlist