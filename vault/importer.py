import csv
from .database import get_connection
from .crypto import encrypt

def import_csv(path: str, key):
    conn = get_connection()
    c = conn.cursor()
    with open(path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            service = row['service']
            username = encrypt(row['username'], key)
            password = encrypt(row['password'], key)
            c.execute("""
                INSERT OR REPLACE INTO credentials (service, username, password)
                VALUES (?, ?, ?)
            """, (service, username, password))
    conn.commit()
    conn.close()
