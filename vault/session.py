import os
from .config import SALT_PATH
from .crypto import generate_key, encrypt, decrypt
from .database import get_connection
from .database import init_db

def create_salt():
    salt = os.urandom(16)
    with open(SALT_PATH, "wb") as f:
        f.write(salt)
    return salt

def load_salt():
    if not os.path.exists(SALT_PATH):
        return create_salt()
    with open(SALT_PATH, "rb") as f:
        return f.read()

def setup_vault(master_password: str):
    init_db()
    salt = create_salt()
    key = generate_key(master_password, salt)
    # Store verification token
    conn = get_connection()
    c = conn.cursor()
    token = encrypt("VAULT_UNLOCK_OK", key)
    c.execute("INSERT INTO verification (token) VALUES (?)", (token,))
    conn.commit()
    conn.close()
    return key

def verify_master_password(master_password: str):
    salt = load_salt()
    key = generate_key(master_password, salt)
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT token FROM verification LIMIT 1")
    row = c.fetchone()
    conn.close()
    if not row:
        raise Exception("Vault not initialized.")
    try:
        decrypted = decrypt(row[0], key)
        if decrypted != "VAULT_UNLOCK_OK":
            raise ValueError
    except:
        raise ValueError("Incorrect master password")
    return key
