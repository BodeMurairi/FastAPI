#!/usr/bin/env python3

from model.creature import Explorer

_explorers = [
    Explorer(name ="Claude Hande",
             country="FR",
             description="Scarce during full moons"),
    Explorer(name = "Noah Waiser",
             country="USA",
             description="Myopic machete man")
    ]

def get_all() -> list[Explorer]:
    "get all explorers"
    return _explorers

def get_one(name:str) -> Explorer | None:
    "get one explorer by name"
    for _explorer in _explorers:
        if _explorer.name == name:
            return _explorer
        else:
            return None

def create_explorer(explorer:Explorer) -> Explorer:
    """Add an explorer"""
    return explorer

def modify(explorer:Explorer) -> Explorer:
    "Partially modify an explorer"
    return explorer

def replace(explorer:Explorer) -> Explorer:
    "replace an explorer"
    return explorer

def delete(name:str) -> bool:
    "delete an explorer. return None if not existant"
    return bool
