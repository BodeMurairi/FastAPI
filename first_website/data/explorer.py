#!/usr/bin/env python3

from .init import conn, curs
from model.explorer import Explorer

# Ensure table exists
curs.execute("""
CREATE TABLE IF NOT EXISTS explorer (
    name TEXT PRIMARY KEY,
    country TEXT,
    description TEXT
)
""")
conn.commit()  # Commit table creation


def row_to_model(row: tuple) -> Explorer:
    """Convert a SQLite row tuple to an Explorer model."""
    return Explorer(name=row[0], country=row[1], description=row[2])


def model_to_dict(explorer: Explorer) -> dict:
    """Convert a Pydantic model to a dictionary for SQLite insertion."""
    return explorer.model_dump()


def get_one(name: str) -> Explorer | None:
    """Get one explorer by name."""
    curs.execute("SELECT * FROM explorer WHERE name=:name", {"name": name})
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    return None


def get_all() -> list[Explorer]:
    """Get all explorers."""
    curs.execute("SELECT * FROM explorer")
    rows = curs.fetchall()
    return [row_to_model(row) for row in rows]


def create(explorer: Explorer) -> Explorer:
    """Insert one explorer into the database."""
    curs.execute(
        "INSERT INTO explorer (name, country, description) VALUES (:name, :country, :description)",
        model_to_dict(explorer)
    )
    conn.commit()
    return get_one(explorer.name)


def modify(name: str, explorer: Explorer) -> Explorer | None:
    """Update one explorer in the database."""
    params = model_to_dict(explorer)
    params["name_orig"] = name
    curs.execute("""
        UPDATE explorer
        SET name=:name,
            country=:country,
            description=:description
        WHERE name=:name_orig
    """, params)
    conn.commit()
    return get_one(explorer.name)


def delete(explorer: Explorer) -> str:
    """Delete one explorer from the database and confirm completion."""
    curs.execute("DELETE FROM explorer WHERE name=:name", {"name": explorer.name})
    conn.commit()
    return f"Explorer '{explorer.name}' has been successfully deleted."
