import sqlite3
from .config import DB_PATH, ensure_vault_dir

ensure_vault_dir()

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS credentials (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        service TEXT NOT NULL,
        username BLOB NOT NULL,
        password BLOB NOT NULL
    )
    """)
    return conn

def add_credential(service, username, password):
    conn = get_connection()
    conn.execute(
        "INSERT INTO credentials (service, username, password) VALUES (?, ?, ?)",
        (service, username, password)
    )
    conn.commit()
    conn.close()

def get_credential(service):
    conn = get_connection()
    cursor = conn.execute(
        "SELECT username, password FROM credentials WHERE service=?",
        (service,)
    )
    row = cursor.fetchone()
    conn.close()
    return row

def list_services():
    conn = get_connection()
    cursor = conn.execute("SELECT service FROM credentials")
    services = [row[0] for row in cursor.fetchall()]
    conn.close()
    return services

def delete_credential(service):
    conn = get_connection()
    conn.execute("DELETE FROM credentials WHERE service=?", (service,))
    conn.commit()
    conn.close()
