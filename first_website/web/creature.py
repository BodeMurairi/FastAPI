#!/usr/bin/env python3

from fastapi import APIRouter
from model.creature import Creature
import fake.creature as service

router = APIRouter(prefix="/creatures")

@router.get("/")
def get_creatures() -> list[Creature]:
    """get all creatures"""
    return service.get_all()

@router.get("/{name}")
def get_creature(name:str) -> Creature|None:
    """get one creature"""
    return service.get_one(name)

@router.post("/")
def create_creature(creature:Creature) -> Creature:
    """create new creature"""
    return service.create(creature)

@router.patch("/")
def modify_creatures(creature:Creature) -> Creature:
    """modify one creature"""
    return service.modify_creature(creature)

@router.put("/")
def replace_creatures(creature:Creature) -> Creature:
    """replace"""
    return service.replace_creature(creature)

@router.delete("/{name}")
def delete_creatures(name:str) -> bool:
    """delete"""
    return service.delete_creature(name)
