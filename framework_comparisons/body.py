#!/usr/bin/env python3

from fastapi import FastAPI
from flask import Flask, jsonify, request

app = FastAPI()
app_2 = Flask(__name__)

@app.get("/hi")
def greet(who:str):
    return f"Hello {who}"

@app_2.route("/bode", methods=["GET"])
def greeting():
    who:str = request.json["who"]
    return jsonify(f"Hello {who}")
