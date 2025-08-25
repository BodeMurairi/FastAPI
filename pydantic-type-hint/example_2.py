#!/usr/bin/env python3
from typing import Any, Union

responses:dict[str, Any] = {"name": "Bode", "score":85}

# more specific
responses_2:dict[str,Union[str,int]] = {"Marco": "Polo", "score":85}
# or with python 3.10+
responses_3:dict[str, str|int] = {"country":"Seychelles",
                                  "capital city": "Victoria",
                                  "population": 1562500}

# for a function
def greeting(name:str) -> str:
    """return a greeting with name"""
    return f"Hello {name}"

def get_thing() -> str:
    "return a random thing"
    return "yetti"
