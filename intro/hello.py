#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def greet():
    return "Hello World"

if __name__ == "__main__":
    uvicorn.run("hello:app", reload=True)
