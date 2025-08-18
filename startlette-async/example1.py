#!/usr/bin/env python3

import asyncio
import time
import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hi")
async def greet():
    await asyncio.sleep(1)
    return "Hello? World"

@app.get("/greet")
def greet_me():
    time.sleep(1)
    return "Hello? World"

if __name__ == "__main__":
    uvicorn.run("example1:app", port=8000)
