from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,validator,Field

app = FastAPI()

class calcInput(BaseModel):
    a:int
    b:int
    operation:str

@app.post("/calculator")
def calculate(inputParams:calcInput):
    if(inputParams.operation == 'add'):
        return inputParams.a+inputParams.b 
    elif(inputParams.operation == 'sub'):
        return inputParams.a-inputParams.b
    elif(inputParams.operation == 'mul'):
        return inputParams.a*inputParams.b 
    elif(inputParams.operation == 'div'):
        if inputParams.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed.")
        return inputParams.a/inputParams.b
    else:
        raise HTTPException(status_code=400,detail="operation is not allowed")
    
