#!/usr/bin/env python3

from collections import namedtuple

# tuple
CreatureNameTuple = namedtuple("CreatureNamedTuple", "name","country", "descriptions", "aka")
namedtuple_thing = CreatureNameTuple("yeti", "CN", "Himalaya", "Hirsute HImalayan", "Abominable Snowman")
print("Name is", namedtuple_thing[0])
print("Name is", namedtuple_thing.name)

# using a standard class
class CreatureClass():
    def __init__(self,
        name:str,
        country:str,
        area:str,
        description:str,
        aka:str
        ):
        self.name = name
        self.country = country
        self.area = area
        self.description = description
        self.aka = aka
