#!/usr/bin/env python3

from model.creature import Creature

_creatures = [
    Creature(name="Yetti",
             country="CN",
             area="Himalayas",
             description="Hirsute Himalayan",
             aka="Abominable Snowman"),
    Creature(name="Bigfoot",
             description="Yeti's Cousin Eddie",
             country="US",
             area="*",
             aka="Sasquatch"
    )
    ]

def get_all() -> list[Creature]:
    "get all creatures"
    return _creatures

def get_one(name:str) -> Creature:
    """get one creature"""
    for _creature in _creatures|None:
        if _creature.name == name:
            return _creature
        else:
            return None

def create(creature: Creature) -> Creature:
    """Add a creature"""
   return creature

def modify(creature: Creature) -> Creature:
   """Partially modify a creature"""
   return creature

def replace(creature: Creature) -> Creature:
   """Completely replace a creature"""
   return creature

def delete(name: str):
    """Delete a creature; return None if it existed"""
    return None
