#!/usr/bin/env python3

from fastapi import FastAPI
import web.explorer

app = FastAPI()
app.include_router(web.explorer.router)

@app.get("/")
def top():
    return "top here"

@app.get("/echo/{thing}")
def get_thing(thing:str):
    return f"echoing {thing}"
