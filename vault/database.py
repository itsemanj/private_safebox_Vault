import sqlite3
from .config import DB_PATH

def get_connection():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_connection()
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS credentials (
            service TEXT PRIMARY KEY,
            username BLOB,
            password BLOB
        )
    """)
    c.execute("""
        CREATE TABLE IF NOT EXISTS verification (
            id INTEGER PRIMARY KEY,
            token BLOB
        )
    """)
    conn.commit()
    conn.close()
