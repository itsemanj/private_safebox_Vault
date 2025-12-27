import sys
from .session import setup_vault, verify_master_password
from .database import get_connection, init_db
from .crypto import encrypt, decrypt
from .importer import import_csv
from tabulate import tabulate

def main():
    print("Welcome to Self-Vault 🔐")
    choice = input("Do you want to (1) Initialize vault or (2) Unlock existing? [1/2]: ").strip()
    if choice == "1":
        pw = input("Create master password: ").strip()
        pw2 = input("Confirm master password: ").strip()
        if pw != pw2:
            print("Passwords do not match. Exiting.")
            sys.exit(1)
        key = setup_vault(pw)
        print("Vault created successfully!")
    elif choice == "2":
        pw = input("Enter master password: ").strip()
        try:
            key = verify_master_password(pw)
            print("Vault unlocked 🔓")
        except ValueError:
            print("Incorrect master password.")
            sys.exit(1)
    else:
        print("Invalid choice.")
        sys.exit(1)

    # Interactive REPL
    while True:
        cmd = input("vault> ").strip()
        if cmd == "exit":
            print("Vault locked 🔒")
            break
        elif cmd == "add":
            service = input("Service name: ").strip()
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            conn = get_connection()
            c = conn.cursor()
            c.execute("INSERT OR REPLACE INTO credentials (service, username, password) VALUES (?, ?, ?)",
                      (service, encrypt(username, key), encrypt(password, key)))
            conn.commit()
            conn.close()
            print(f"{service} saved ✔")
        elif cmd == "list":
            conn = get_connection()
            c = conn.cursor()
            c.execute("SELECT service FROM credentials")
            rows = c.fetchall()
            conn.close()
            if rows:
                print(tabulate(rows, headers=["Service"]))
            else:
                print("No credentials stored.")
        elif cmd == "get":
            service = input("Enter service name: ").strip()
            conn = get_connection()
            c = conn.cursor()
            c.execute("SELECT username, password FROM credentials WHERE service = ?", (service,))
            row = c.fetchone()
            conn.close()
            if row:
                try:
                    username = decrypt(row[0], key)
                    password = decrypt(row[1], key)
                    print(f"Username: {username}")
                    print(f"Password: {password}")
                except Exception:
                    print("Error: Unable to decrypt. Did you enter the correct master password?")
            else:
                print("Service not found.")
        elif cmd.startswith("import"):
            path = input("Enter CSV file path: ").strip()
            import_csv(path, key)
            print("CSV imported successfully ✔")
        else:
            print("Commands: add, list, get, import, exit")

if __name__ == "__main__":
    main()
