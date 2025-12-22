import os

VAULT_DIR = os.path.join(os.path.expanduser("~"), ".self_vault")
DB_PATH = os.path.join(VAULT_DIR, "vault.db")
SALT_PATH = os.path.join(VAULT_DIR, "vault_salt.bin")

def ensure_vault_dir():
    if not os.path.exists(VAULT_DIR):
        os.makedirs(VAULT_DIR, exist_ok=True)
