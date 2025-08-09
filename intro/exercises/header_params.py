#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Header, HTTPException

app = FastAPI()

@app.get("/secure-data")
def grant_access(token:str=Header(..., description="Authentication token", alias="X-API-Token")):
    """Authentication"""
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Wrong Token")
    else:
        return {"status": "Access granted"}

if __name__ == "__main__":
    uvicorn.run("header_params:app", reload=True)
