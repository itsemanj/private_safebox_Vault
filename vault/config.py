import os

HOME = os.path.expanduser("~/.self_vault")
DB_PATH = os.path.join(HOME, "vault.db")
SALT_PATH = os.path.join(HOME, "vault_salt.bin")

os.makedirs(HOME, exist_ok=True)
