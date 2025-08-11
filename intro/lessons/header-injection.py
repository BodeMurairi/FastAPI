#!/usr/bin/env python3

import uvicorn
from fastapi import Response, FastAPI

app = FastAPI()

@app.get("/header/{name}/{value}")
def header(name:str, value:str, response: Response):
    """
    Set a custom header with the provided name and value
    """
    response.headers[name] = value
    return "normal body"

if __name__ == "__main__":
    uvicorn.run(app, port=8000)
