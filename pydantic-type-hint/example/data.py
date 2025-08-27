#!/usr/bin/env python3

from model import Creature

_creatures:list[Creature] = [
    Creature(name="yeti",
             country="UK",
             area="Bismus",
             description="None",
             aka="valentino"),
    Creature(name="Valence",
             country="SP",
             area="Madridrismus",
             description="MPLR",
             aka="Volt bolt"),
    Creature(name="Irak",
             country="['Flask', 'FastAPI', 'Django']",
             area="Chrty",
             description="*",
             aka="*"),
    Creature(country="Tanzania",
             area="yes",
             description="volant",
             aka="25")
             ]

def get_creatures() -> list[Creature]:
    """Get all creatures"""
    return _creatures
