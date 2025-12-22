import os
import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet

def generate_salt():
    return os.urandom(16)

def generate_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),  
    length=32,
    salt=salt,
    iterations=390000,
)

    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))

def encrypt(data: str, key: bytes) -> bytes:
    return Fernet(key).encrypt(data.encode())

def decrypt(token: bytes, key: bytes) -> str:
    return Fernet(key).decrypt(token).decode()
