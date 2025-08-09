#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/greet")
def greeting(name:str, age:int=Query(18, ge=18)):
    """return a hello message from query parameters"""
    return {"message":f"Hello {name}, you are {age} years old"}


if __name__ == "__main__":
    uvicorn.run("query_params:app", port=8000, reload=True)
