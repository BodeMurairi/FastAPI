#!/usr/bin/env python3

from fastapi import APIRouter, status, HTTPException
from model.creature import Creature
import data.creature as service
from data.error import Missing, Duplicate

router = APIRouter(prefix="/creatures")

@router.get("/")
def get_creatures() -> list[Creature]:
    """get all creatures"""
    return service.get_all()

@router.get("/{name}")
def get_creature(name:str) -> Creature|None:
    """get one creature"""
    try:
        return service.get_one(name)
    except Missing as exc:
        raise HTTPException(status_code=404, detail=exc.msg)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_creature(creature:Creature) -> Creature:
    """create new creature"""
    try:
        return service.create(creature)
    except Duplicate as exc:
        raise HTTPException(status_code=404, detail=exc.msg)
    return service.create(creature)

@router.patch("/")
def modify_creatures(creature:Creature) -> Creature:
    """modify one creature"""
    return service.modify(creature)

@router.delete("/{name}")
def delete_creatures(name:str) -> bool:
    """delete"""
    return service.delete(name)
