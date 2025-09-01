#!/usr/bin/env python3

from fastapi import FastAPI
from flask import Flask, jsonify

app = FastAPI()
app_2 = Flask(__name__)

@app.get("/{who}")
async def hello(who:str):
    """Hello world with fastapi"""
    return f"Hello {who}" # automatic serialization to json

@app_2.route("/<who>", methods=["GET"])
def hello_world(who):
    """hello world with flask"""
    return jsonify(f"hello {who}") # jsonify to return a json response
