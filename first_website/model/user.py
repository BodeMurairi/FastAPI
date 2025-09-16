#!/usr/bin/env python3

from pydantic import BaseModel

class User(BaseModel):
    name:str
    hash_password:str
