#!/usr/bin/env python3

from pydantic import BaseModel

class Explorer(BaseModel):
    name:str
    country:str
    description:str

class Creature(BaseModel):
    name:str
    country:str
    area:str
    description:str
    aka:str
