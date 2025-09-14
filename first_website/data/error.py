#!/usr/bin/env python3

class Missing(Exception):
    def __init__(self, msg:str):
        self.msg = msg

class Duplicate(Exception):
    def __init__(self, msg):
        self.msg = msg
