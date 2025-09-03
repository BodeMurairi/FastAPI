#!/usr/bin/env python3

from fastapi import FastAPI
from flask import Flask, request, jsonify

app = FastAPI()

app2 = Flask(__name__)

@app.get("/hi")
async def greeting(who:str):
    return f"Hello {who}"

@app2.route("/hi/flask")
def greeting_two(who):
    who:str = request.args.get("who")
    return jsonify(f"Hello {who}")
