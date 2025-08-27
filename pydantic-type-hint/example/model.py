#!/usr/bin/env python3

from pydantic import BaseModel, Field

class Creature(BaseModel):
    """Base Model for creature"""
    name:str = Field(default="Bode", min_length=4)
    country:str
    area:str
    description:str
    aka:str
