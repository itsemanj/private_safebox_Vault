# 🔐 Self-Vault: Personal Encrypted Password Manager (CLI)

A **secure, self-contained password vault** written in Python.
All credentials are encrypted locally using **AES encryption** with a master password-derived key.
No plaintext credentials are ever stored, and the database is stored locally using **SQLite**.

This is perfect for personal use and can be cloned from GitHub for your own vault.

---

## ✨ Features

* 🔒 AES-256 encryption with **PBKDF2HMAC key derivation**
* 🧠 Master password authentication
* 🗄️ SQLite-backed storage, fully self-contained
* 💻 Interactive CLI, no coding required
* ✅ Non-coder friendly commands
* 🪄 Dynamic: no hardcoded credentials

---

## 📦 Project Structure

```
self-vault/
│
├── vault/
│   ├── __init__.py
│   ├── cli.py        # CLI commands
│   ├── auth.py       # Master password handling
│   ├── crypto.py     # Encryption / decryption
│   ├── database.py   # SQLite storage
│   └── config.py     # Paths for DB and salt
│
├── setup.py          # Install CLI entry point
├── requirements.txt  # Python dependencies
└── README.md
```

---

## 🛠 Requirements

* Python 3.9+
* `cryptography` library

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ⚡ Installation

1. Clone the repository:

```bash
git clone https://github.com/itsemanj/private_safebox_Vault.git
cd personal\ vault
```

2. Install in **editable mode** (recommended during development):

```bash
pip install -e .
```

This allows any code changes to take effect immediately.

3. Verify the CLI command works:

```bash
vault help
```

---

## 🧩 CLI Commands

| Command        | Description                                   |
| -------------- | --------------------------------------------- |
| `vault init`   | Create a new vault and set a master password  |
| `vault login`  | Unlock the vault (prompt for master password) |
| `vault add`    | Add a new service credential interactively    |
| `vault list`   | List all saved services                       |
| `vault get`    | Retrieve username & password for a service    |
| `vault delete` | Delete a service from the vault               |
| `vault help`   | Show all available commands                   |

---

## 🏃 Example Usage

```bash
vault init
# Create your master password
```

```bash
vault add
# Service name: Gmail
# Username: myemail@gmail.com
# Password: ********
# Saved ✔
```

```bash
vault list
# Output:
# Gmail
# GitHub
# Netflix
```

```bash
vault get
# Enter service name to retrieve: Gmail
# Output:
# Username: myemail@gmail.com
# Password: ********
```

```bash
vault delete
# Enter service name to delete: Gmail
# Deleted ✔
```

---

## 🔐 Security Notes

* The **master password** is never stored. It is used only to derive the encryption key.
* The database (`vault.db`) and salt (`vault_salt.bin`) are stored locally in:

```
~/.self_vault/
```

* Losing the salt or master password **will prevent access to all stored credentials**.
* SQLite file is encrypted, so even if stolen, the contents are protected.

---

## 💡 Tips

* Use a **strong, unique master password**.
* Back up `vault_salt.bin` securely.
* Do not share your vault database file or salt.
* For non-coders, all interactions are via simple CLI commands — no Python editing required.

---

## 🚀 Next Steps / Enhancements

* Add **password generator** for new credentials
* Add **auto-lock** after inactivity
* Export/import encrypted vaults
* GUI version (Tkinter or PyQt)
* Support cloud syncing with end-to-end encryption

---

## ⚠️ Disclaimer

This project is **for personal use and learning purposes**.
Always audit and harden security before using for sensitive or production data.

