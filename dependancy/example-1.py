#!/usr/bin/env python3

from fastapi import FastAPI, Depends, params


app = FastAPI()

# dependancy function
def user_depend(name:str = params, password:str = params)-> dict:
    """user depend"""
    return {"name":name, "valid": True}

@app.get("/user")
def get_user(user:dict = Depends(user_depend)) -> dict:
    return user
