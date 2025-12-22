import sys
from .auth import create_master_password, load_key
from .crypto import encrypt, decrypt
from .database import add_credential, get_credential, list_services, delete_credential

def cmd_init():
    create_master_password()

def cmd_add():
    key = load_key()
    if not key:
        return
    service = input("Service name: ")
    username = input("Username: ")
    password = input("Password: ")
    encrypted_user = encrypt(username, key)
    encrypted_pass = encrypt(password, key)
    add_credential(service, encrypted_user, encrypted_pass)
    print("Credential saved ✔")

def cmd_list():
    key = load_key()
    if not key:
        return
    services = list_services()
    if not services:
        print("No credentials saved yet.")
    else:
        for s in services:
            print(s)

def cmd_get():
    key = load_key()
    if not key:
        return
    service = input("Enter service name to retrieve: ")
    row = get_credential(service)
    if row:
        username = decrypt(row[0], key)
        password = decrypt(row[1], key)
        print(f"Username: {username}\nPassword: {password}")
    else:
        print("Service not found.")

def cmd_delete():
    key = load_key()
    if not key:
        return
    service = input("Enter service name to delete: ")
    delete_credential(service)
    print("Deleted ✔")

def print_help():
    print("""
Available commands:
init    - Create your vault / master password
add     - Add new credentials
list    - List all services
get     - Retrieve credentials for a service
delete  - Delete a service
help    - Show this message
""")

def main():
    if len(sys.argv) < 2:
        print_help()
        return
    cmd = sys.argv[1].lower()
    if cmd == "init":
        cmd_init()
    elif cmd == "add":
        cmd_add()
    elif cmd == "list":
        cmd_list()
    elif cmd == "get":
        cmd_get()
    elif cmd == "delete":
        cmd_delete()
    elif cmd == "help":
        print_help()
    else:
        print("Unknown command")
        print_help()

if __name__ == "__main__":
    main()
