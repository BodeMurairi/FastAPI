#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI, Body
from pydantic import BaseModel, EmailStr, Field

app = FastAPI()

class UserRegistration(BaseModel):
    """Base Model for user registration"""
    username:str = Field(..., min_length=3)
    email:EmailStr = Field(..., min_length=8)
    password:str = Field(..., min_length=8)

@app.post("/register")
def register(user1:UserRegistration=Body()):
    """Register new user"""
    return {"message": f"User {user1.username} registered successfully"}

if __name__ == "__main__":
    uvicorn.run("body_parameters:app", reload=True)
