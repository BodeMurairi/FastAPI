#!/usr/bin/env python3

from model.user import User
from data.error import Missing, Duplicate

fakes = [
    User(name="Kwijobo", hash_password="abc"),
    User(name="bode", hash_password="bode"),
    User(name="alexandra", hash_password="bcd")
]

def find(name:str) -> User|None:
    """find a user"""
    for e in fakes:
        if e.name == name:
            return e
    return None

def check_missing(name:str):
    """check for missing"""
    if not find(name):
        raise Missing(msg=f"Missing user {name}")

def check_duplicate(name:str):
    """check for duplicate"""
    if find(name):
        raise Duplicate(msg=f"duplicate {name}")

def get_all() -> list[User]:
    """Return all users"""
    return fakes

def get_one(name: str) -> User:
    """Return one user"""
    check_missing(name)
    return find(name)

def create(user: User) -> User:
    """Add a user"""
    check_duplicate(user.name)
    return user

def modify(name: str, user: User) -> User:
    """Partially modify a user"""
    check_missing(name)
    return user

def delete(name: str) -> None:
    """Delete a user"""
    check_missing(name)
    return None
