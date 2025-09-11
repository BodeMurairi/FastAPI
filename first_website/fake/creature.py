#!/usr/bin/env python3

from model.creature import Creature

_creatures: list[Creature] = [
    Creature(
        name="Yetti",
        country="CN",
        area="Himalayas",
        description="Hirsute Himalayan",
        aka="Abominable Snowman"
    ),
    Creature(
        name="Bigfoot",
        description="Yeti's Cousin Eddie",
        country="US",
        area="*",
        aka="Sasquatch"
    )
]

def get_all() -> list[Creature]:
    """Get all creatures"""
    return _creatures

def get_one(name: str) -> Creature | None:
    """Get one creature by name"""
    for _creature in _creatures:
        if _creature.name.lower() == name.lower():
            return _creature
    return None

def create(creature: Creature) -> Creature:
    """Add a creature"""
    # Prevent duplicates
    if any(c.name.lower() == creature.name.lower() for c in _creatures):
        return creature
    _creatures.append(creature)
    return creature

def modify_creature(name: str, updates: dict) -> Creature | None:
    """Update fields of an existing creature"""
    for idx, _creature in enumerate(_creatures):
        if _creature.name.lower() == name.lower():
            data = _creature.dict()
            data.update(updates)
            updated = Creature(**data)
            _creatures[idx] = updated
            return updated
    return None

def replace_creature(name: str, creature: Creature) -> Creature | None:
    """Completely replace an existing creature"""
    for idx, _creature in enumerate(_creatures):
        if _creature.name.lower() == name.lower():
            _creatures[idx] = creature
            return creature
    return None

def delete_creature(name: str) -> bool:
    """Delete a creature by name"""
    for idx, _creature in enumerate(_creatures):
        if _creature.name.lower() == name.lower():
            del _creatures[idx]
            return True
    return False
