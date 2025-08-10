from fastapi import FastAPI
from pydantic import BaseModel,Field,validator

app = FastAPI()

class NumberModel(BaseModel):
    a:int
    b:int

@app.get("/")
def add(a:int,b:int):
    return a+b

@app.post("/sub")
def sub(nums:NumberModel):
    return nums.a-nums.b

@app.post("/multiply")
def multiply(nums:NumberModel):
    return nums.a*nums.b