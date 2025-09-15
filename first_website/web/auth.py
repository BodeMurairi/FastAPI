#!/usr/bin/env python3

import uvicorn
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

secret_usr: str = "bodemurairi"
secret_password: str = "murairi"

basic: HTTPBasicCredentials = HTTPBasic()

@app.get("/who")
def get_users(creds: HTTPBasicCredentials = Depends(basic))->dict:
    """get user"""
    if (creds.username == secret_usr and creds.password == secret_password):
        return {"username": creds.username, "password": creds.password}
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid Username or Password")

if __name__ == "__main__":
    uvicorn.run(
        "auth:app", reload=True
    )
