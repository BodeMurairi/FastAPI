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

def get_one(name:str) -> Creature|None:
    """get one creature"""
    for _creature in _creatures:
        if _creature.name == name:
            return _creature
        else:
            return None

def create(creature: Creature) -> Creature|None:
    """Add a creature"""
    for _creature in _creatures:
        if _creature == creature:
            return _creature
        else:
            return None

def modify_creature(creature: Creature) -> Creature|None:
    """Add a creature"""
    for _creature in _creatures:
        if _creature == creature:
            return _creature
        else:
            return None

def replace_creature(creature: Creature) -> Creature|None:
    """Add a creature"""
    for _creature in _creatures:
        if _creature == creature:
            return _creature
        else:
            return None

def delete_creature(creature: Creature) -> Creature|None:
    """Add a creature"""
    for _creature in _creatures:
        if _creature == creature:
            return _creature
        else:
            return None
