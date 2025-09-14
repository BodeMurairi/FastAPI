#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from pathlib import Path
from sqlite3 import connect, Connection, Cursor, IntegrityError

load_dotenv("config.env")

conn: Connection | None = None
curs: Cursor | None = None

def get_db(name: str | None = None, reset: bool = False) -> tuple[Connection, Cursor]:
    """Connect to SQLite database, creating folders if necessary."""
    global conn, curs

    if conn and curs and not reset:
        return conn, curs

    if not name:
        env_path = os.getenv("CRYPTID_SQLITE_DB")
        if env_path:
            db_path = Path(env_path).resolve()
        else:
            top_dir = Path(__file__).resolve().parents[1]
            db_path = top_dir / "db" / "cryptid.db"
        db_path.parent.mkdir(parents=True, exist_ok=True)
        name = str(db_path)

    conn = connect(name, check_same_thread=False)
    curs = conn.cursor()

    return conn, curs

# Initialize global connection and cursor
conn, curs = get_db()
