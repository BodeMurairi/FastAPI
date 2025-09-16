#!/usr/bin/env python3

from model.user import User
from data.init import (conn, curs, get_db, IntegrityError)
from data.error import Missing, Duplicate

curs.execute("""create table if not exists
             user(
             name text primary key,
             hash_password text)""")

curs.execute("""create table if not exists
             delete_user(
             name text primary key,
             hash_password primary key)""")


def row_to_model(row:tuple) -> User:
    name, hash = row
    return User(name=name, hash_password=hash)

def model_to_dict(user:User)->dict:
    return user.model_dump()

def get_user(name:str)->str:
    qry = "select * from user where name=:name"
    params = {"name":name}
    curs.execute(qry,params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"User {name} not found")

def get_users()->list[User]:
    query = "select * from User"
    curs.execute(query)
    return [row_to_model(row) for row in curs.fetchall()]

def create_user(user:User, table:str= "user"):
    """Add user to user or delete_user"""
    query = f"""insert into {table}
        (name, hash_password)
        values
        (:name, :hash_password)"""
    params = model_to_dict(user)
    try:
        curs.execute(query, params)
    except IntegrityError:
        raise Duplicate(msg=f"{table}:user {user.name} already exists")

def modify(name:str, user:User)->User:
    query = """update user set
            name=:name, hash_password=:hash
            where name=:name0"""
    params= {
        "name":user.name,
        "hash_password":user.hash_password,
        "name0":name
    }
    curs.execute(query,params)
    if curs.rowcount == 1:
        return get_user(user.name)
    else:
        raise Missing(msg=f"user {name} not found")

def delete(name:str) -> bool|None:
    """Drop user with <name> from table, add to delete_table"""
    user = get_user(name)
    query = "delete from user where name=:name"
    params = {"name":name}
    curs.execute(query, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"User {name} not found")
    create_user(user, table="delete_user")
