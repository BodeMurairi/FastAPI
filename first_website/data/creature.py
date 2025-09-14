#!/usr/bin/env python3

from .init import (conn, curs, IntegrityError)
from model.creature import Creature
from .error import Missing, Duplicate

# Ensure table exists
curs.execute("""
CREATE TABLE IF NOT EXISTS creature (
    name TEXT PRIMARY KEY,
    description TEXT,
    country TEXT,
    area TEXT,
    aka TEXT
)
""")
conn.commit()  # Commit table creation


def row_to_model(row: tuple) -> Creature:
    """Convert a SQLite row tuple to a Creature model."""
    name, description, country, area, aka = row
    return Creature(name=name, description=description, country=country, area=area, aka=aka)


def model_to_dict(creature: Creature) -> dict:
    """Convert a Pydantic model to a dictionary for SQLite insertion."""
    return creature.model_dump()


def get_one(name: str) -> Creature | None:
    """Get one creature by name."""
    curs.execute("SELECT * FROM creature WHERE name=:name", {"name": name})
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Creature {name} not found")

def get_all() -> list[Creature]:
    """Get all creatures."""
    curs.execute("SELECT * FROM creature")
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(creature: Creature) -> Creature:
    """Insert one creature into the database."""
    try:
        curs.execute(
        "INSERT INTO creature VALUES (:name, :description, :country, :area, :aka)",
        model_to_dict(creature)
        )
        conn.commit()
    except IntegrityError:
        raise Duplicate(f"Creature {creature.name} already exists")
    return get_one(creature.name)


def modify(creature: Creature) -> Creature:
    """Update one creature in the database."""
    params = model_to_dict(creature)
    params["name_orig"] = creature.name
    curs.execute("""
        UPDATE creature
        SET name=:name,
            description=:description,
            country=:country,
            area=:area,
            aka=:aka
        WHERE name=:name_orig
    """, params)
    conn.commit()
    return get_one(creature.name)


def delete(creature: Creature) -> bool:
    """Delete one creature from the database."""
    curs.execute("DELETE FROM creature WHERE name=:name", {"name": creature.name})
    conn.commit()
    return f"Explorer '{creature.name}' has been successfully deleted."
