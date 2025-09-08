#!/usr/bin/env python3

from typing import List, Dict
from models.creature import Creature
import fake.creature as fake_creature

def get_all_creatures() -> List[Creature]:
    """Retrieve all creatures. """
    return fake_creature.get_all_creatures()

def get_creature_by_name(name:str) -> Creature|None:
    """Retrieve a creature by its name"""
    return fake_creature.get_one(name)

def create_creature(creature_dict:Creature) -> Creature:
    """Create a new creature"""
    return fake_creature.create(creature_dict)

def replace_creature(id:int, creature_dict:Creature) -> Creature|None:
    """Replace an existing creature"""
    return fake_creature.replace_creature(id, creature_dict)

def update_creature(id:int, creature_dict:Dict) -> Creature|None:
    """Update an existing creature"""
    return fake_creature.modify_creature(id, creature_dict)

def delete_creature(id:int) -> bool:
    """Delete a creature"""
    return fake_creature.delete_creature(id)
