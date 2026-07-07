# Finance Engine Architecture

## Current Project Structure

finance_engine/

├── db.py
├── create_tables.py
├── vendor.py
├── category.py
├── transaction.py
├── scratch.py
├── finance.db
└── docs/

## Module Responsibilities

### db.py

Creates the SQLite database connection and cursor.

Responsible for:
- Opening database connection
- Enabling foreign keys
- Returning connection and cursor

---

### vendor.py

Responsible for vendor management.

Features:
- Find existing vendor aliases
- Create vendors
- Create aliases
- Return vendor_id

---

### category.py

Responsible for category lookup.

Features:
- Returns category_id
- Does NOT create categories

---

### transaction.py

Responsible for transaction creation.

Features:
- Receives transaction details
- Resolves vendor_id
- Resolves category_id
- Inserts transaction
- Owns the database transaction
- Performs commit