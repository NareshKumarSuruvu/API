from fastapi import FastAPI
from pydantic import BaseModel,Field

app = FastAPI()

user_db = {
    1:{"name":"Naresh","age":30},
    2:{"name":"kumar","age":24},
    3:{"name":"saradi","age":33},
}

class User(BaseModel):
    name:str
    age:int 

@app.put("/update/{user_id}")
def update(user_id:int,user:User):
    if user_id in user_db :
        user_db[user_id] = user.model_dump()
        print(user_db)
        return {"status":"success","msg":"user details updated successfully"}

    else :
        return {"status":"error","msg":"user details not found"}
    
@app.delete("/delete/{user_id}")
def delete(user_id:int):
    if user_id in user_db :
        del user_db[user_id]
        print(user_db)
        return {"status":"success","msg":"user deleted successfully"}
    else:
         return {"status":"error","msg":"user details not found"}
    

