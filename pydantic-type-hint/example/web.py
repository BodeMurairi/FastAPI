#!/usr/bin/env python3

from model import Creature
from fastapi import FastAPI
from data import get_creatures

app = FastAPI()

@app.get("/creatures")
def get_all() -> list[Creature]:
    """get all creatures"""
    return get_creatures()

