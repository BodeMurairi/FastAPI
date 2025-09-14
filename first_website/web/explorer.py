#!/usr/bin/env python3

from fastapi import APIRouter, status
from model.explorer import Explorer
import data.explorer as service

router = APIRouter(prefix= "/explorer")

@router.get("/")
def get_all() -> list[Explorer]:
    return service.get_all()

@router.get("/{name}")
def get_one(name:str) -> Explorer|None:
    return service.get_one(name)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_explorer(explorer:Explorer) -> Explorer:
    return service.create(explorer)

@router.patch("/")
def modify(explorer:Explorer) -> Explorer:
    return service.modify(explorer)

@router.delete("/{name}")
def delete(name:str) -> Explorer:
    return service.delete(name)
