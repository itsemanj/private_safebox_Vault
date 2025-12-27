# Self-Vault

A **secure, local password manager** for storing and managing usernames and passwords safely.
All data is encrypted and can only be accessed with your **master password**.

---

## Features

* Vault unlocks with **one master password** per session.
* Master password **cannot be changed** — if forgotten, all data is lost.
* Store credentials for multiple services securely (Service, Username, Password).
* Interactive CLI: add, list, get, import, exit.
* Bulk import credentials via **CSV file**.
* Displays all credentials in a **clean table format**.

---

## Security Notes

* **AES-256 encryption** with PBKDF2-derived key.
* Master password is never stored.
* Vault is fully **private** — only accessible with the correct master password.
* Forgetting the master password means the vault **cannot be recovered**.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/self-vault.git
cd self-vault
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Install the CLI tool locally:

```bash
pip install -e .
```

---

## Usage

Run the vault:

```bash
vault
```

### Step 1: Initialize or Unlock Vault

* **Initialize**: Set your master password (first time use).
* **Unlock**: Enter the existing master password.

---

### Step 2: Commands

Once inside the vault session:

| Command  | Description                                                      |
| -------- | ---------------------------------------------------------------- |
| `add`    | Add a new credential (Service, Username, Password)               |
| `list`   | List all stored credentials in a table                           |
| `import` | Import credentials from a CSV file (`service,username,password`) |
| `exit`   | Exit the vault session                                           |

Example:

```text
vault> add
Service name: GitHub
Username: me@gmail.com
Password: secret123
GitHub saved successfully! ✔

vault> list
Service    Username        Password
--------   ---------       ---------
GitHub     me@gmail.com    secret123

vault> exit
Vault locked 🔒
```

---

### Step 3: CSV Import Format

Your CSV file should have **headers**:

```csv
service,username,password
GitHub,me@gmail.com,secret123
Google,user@gmail.com,password456
```

Use the `import` command in the vault to load credentials:

```text
vault> import
Enter CSV file path: /path/to/credentials.csv
CSV imported successfully! ✔
```

---

## Project Structure

```
self-vault/
│
├── vault/
│   ├── cli.py          # Main interactive CLI
│   ├── session.py      # Master password setup and verification
│   ├── crypto.py       # AES encryption/decryption
│   ├── database.py     # SQLite DB management
│   ├── importer.py     # CSV import
│   └── config.py       # Paths for DB and salt
├── setup.py
├── requirements.txt
└── README.md
```

---

## Dependencies

* Python 3.8+
* [cryptography](https://cryptography.io/)
* [tabulate](https://pypi.org/project/tabulate/)

Install via:

```bash
pip install cryptography tabulate
```

---

## Important Notes

* **Do not forget your master password** — there is no password recovery.
* Vault data is stored locally in your home directory (`~/.self_vault/vault.db`).
* For maximum security, keep your DB and salt file private.

