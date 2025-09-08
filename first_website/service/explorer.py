#!/usr/bin/env python3

from typing import List, Dict
from model.explorer import Explorer
import fake.explorer as fake_explorer

def get_explorers() -> List[Dict]:
    return fake_explorer.get_all()

def get_explorer(name: str) -> Explorer|None:
    return fake_explorer.get_one(name)

def create_explorer(explorer: Explorer) -> Explorer:
    return fake_explorer.create_explorer(explorer)

def modify_explorer(explorer:Explorer) -> Explorer:
    return fake_explorer.modify(explorer)

def replace_explorer(explorer:Explorer) -> Explorer:
    return fake_explorer.replace(explorer)

def delete_explorer(name:str) -> bool:
    return fake_explorer.delete(name)
