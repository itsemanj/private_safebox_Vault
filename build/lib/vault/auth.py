import os
from .config import SALT_PATH, ensure_vault_dir
from .crypto import generate_salt, generate_key

def create_master_password():
    ensure_vault_dir()
    if os.path.exists(SALT_PATH):
        print("Vault already initialized.")
        return
    pwd1 = input("Create a master password: ")
    pwd2 = input("Confirm master password: ")
    if pwd1 != pwd2:
        print("Passwords do not match. Try again.")
        return create_master_password()
    salt = generate_salt()
    with open(SALT_PATH, "wb") as f:
        f.write(salt)
    print("Vault created successfully! 🔐")

def load_key():
    if not os.path.exists(SALT_PATH):
        print("Vault not initialized. Run 'vault init' first.")
        return None
    salt = open(SALT_PATH, "rb").read()
    master_password = input("Enter master password: ")
    key = generate_key(master_password, salt)
    return key
