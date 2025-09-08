#!/usr/bin/env python3
import uvicorn
from fastapi import FastAPI
from web import creature, explorer

app = FastAPI()
app.include_router(explorer.router)
app.include_router(creature.router)

@app.get("/")
def top():
    "top"
    return "top here"

@app.get("/echo/{thing}")
def get_thing(thing:str):
    "things"
    return f"echoing {thing}"

if __name__ == "__main__":
    uvicorn.run("web.main:app", reload=True)
