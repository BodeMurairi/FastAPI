#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get("/")
async def greet():
    return "Hello World"

# path parameters
@app.get("/hello/{who}")
async def greetSomeone(who):
    return f"Hello Mr/Ms.{who}"

# query parameters
@app.get("/hello")
async def queryGreet(who):
    return f"Hello Mr/Ms.{who}"

# body parameter
@app.post("/hi")
async def send_greet(who:str = Body(embed=True)):
    return f"Hello {who}"

# header parameter
@app.post("/greeting")
async def header_greet(who:str = Header()):
    return f"Hello {who}"

# print user agent
@app.post("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent

# test status code
@app.get("/happy")
def happy(status_code=200):
    return ":)"

if __name__ == "__main__":
    uvicorn.run("hello:app", reload=True)
