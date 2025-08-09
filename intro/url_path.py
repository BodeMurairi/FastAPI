#!/usr/bin/env python3

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{who}")
async def greet(who):
    return f"hello {who}"

if __name__ == "__main__":
    uvicorn.run("url_path:app",
                reload=True,
                port=8000)
