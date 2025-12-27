import sys
from tabulate import tabulate
from .session import setup_vault, verify_master_password
from .database import get_connection, init_db
from .crypto import encrypt, decrypt
from .config import DB_PATH
from .importer import import_csv

def main():
    print("Welcome to Self-Vault 🔐")
    choice = input("Do you want to (1) Initialize vault or (2) Unlock existing? [1/2]: ").strip()
    if choice == "1":
        # Initialize vault
        master_password = input("Create master password: ").strip()
        confirm_password = input("Confirm master password: ").strip()
        if master_password != confirm_password:
            print("Passwords do not match. Exiting.")
            sys.exit(1)
        key = setup_vault(master_password)
        print("Vault created successfully! 🔐\n")
    elif choice == "2":
        # Unlock existing vault
        master_password = input("Enter master password: ").strip()
        try:
            key = verify_master_password(master_password)
            print("Vault unlocked 🔓\n")
        except ValueError:
            print("Incorrect master password. Exiting.")
            sys.exit(1)
    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

    # Interactive vault session (REPL)
    while True:
        cmd = input("vault> ").strip().lower()

        if cmd == "exit":
            print("Vault locked 🔒")
            break

        elif cmd == "add":
            service = input("Service name: ").strip()
            username = input("Username: ").strip()
            password = input("Password: ").strip()
            conn = get_connection()
            c = conn.cursor()
            c.execute("""
                INSERT OR REPLACE INTO credentials (service, username, password)
                VALUES (?, ?, ?)
            """, (service, encrypt(username, key), encrypt(password, key)))
            conn.commit()
            conn.close()
            print(f"{service} saved successfully! ✔\n")

        elif cmd == "list":
            conn = get_connection()
            c = conn.cursor()
            c.execute("SELECT service, username, password FROM credentials")
            rows = c.fetchall()
            conn.close()
            if rows:
                table = []
                for r in rows:
                    try:
                        table.append([r[0], decrypt(r[1], key), decrypt(r[2], key)])
                    except Exception:
                        table.append([r[0], "***ERROR***", "***ERROR***"])
                print(tabulate(table, headers=["Service", "Username", "Password"]))
            else:
                print("No credentials stored.\n")

        elif cmd == "get":
            service = input("Enter service name: ").strip()
            conn = get_connection()
            c = conn.cursor()
            c.execute("SELECT username, password FROM credentials WHERE service = ?", (service,))
            row = c.fetchone()
            conn.close()
            if row:
                try:
                    print(tabulate([[service, decrypt(row[0], key), decrypt(row[1], key)]],
                                   headers=["Service", "Username", "Password"]))
                except Exception:
                    print("Error decrypting this entry. Possibly corrupted.")
            else:
                print("Service not found.\n")

        elif cmd == "import":
            csv_path = input("Enter CSV file path: ").strip()
            try:
                import_csv(csv_path, key)
                print("CSV imported successfully! ✔\n")
            except Exception as e:
                print(f"Error importing CSV: {e}")

        elif cmd == "help":
            print("Available commands: add, list, get, import, exit\n")

        else:
            print("Unknown command. Type 'help' to see commands.\n")

if __name__ == "__main__":
    main()
