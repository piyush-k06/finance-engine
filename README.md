# Finance Engine

A modular personal finance analytics platform built with Python. The project focuses on transaction ingestion, vendor normalization, configurable bank statement import, financial analytics, and a future LLM-powered natural language interface for querying personal finance data.

> 🚧 **Status:** Active Development
>
> Current focus: Configurable import pipeline (CSV/Excel), data validation, and backend architecture for future LLM integration.

---

## Implemented Features

- ✅ Normalized SQLite database schema
- ✅ Vendor management system
- ✅ Vendor alias resolution (e.g., `AMZN` → `Amazon`)
- ✅ Category management
- ✅ Transaction insertion pipeline
- ✅ Foreign key relationships
- ✅ Integration testing
- ✅ Database reset utility
- ✅ Modular project architecture
- ✅ Configuration-driven project structure

---

## Tech Stack

Python • SQLite • SQL • Pandas • Git • GitHub

## Installation

```bash
git clone https://github.com/piyush-k06/finance-engine.git
cd finance-engine
pip install pandas openpyxl

python create_tables.py
```

---

## Project Structure

```
finance_engine/

├── README.md
├── category.py
├── create_tables.py
├── db.py
├── importer.py
├── transaction.py
├── vendor.py
│
├── config/
│   ├── column_map.py
│   ├── constants.py
│   └── settings.py
│
├── docs/
│   ├── architecture.md
│   ├── changelog.md
│   ├── database.md
│   ├── decisions.md
│   ├── interview_notes.md
│   ├── mistakes.md
│   └── roadmap.md
│
├── scripts/
│   └── reset_db.py
```

---

## Database Design

The database is normalized into separate tables to reduce redundancy.

### Tables

- Categories
- Vendors
- Vendor Aliases
- Transactions

Relationships are maintained using **foreign keys**.

---

## Current Workflow

```
Raw Transaction
      │
      ▼
Vendor Alias Lookup
      │
      ▼
Vendor Resolution
      │
      ▼
Category Lookup
      │
      ▼
Transaction Validation
      │
      ▼
Database Insertion
```

---

## Roadmap

### Phase 0 (Completed)

- Database setup
- Categories
- Vendors
- Vendor aliases
- Transaction pipeline
- Integration tests
- Documentation

### Phase 1 (In Progress)

- CSV Import
- Excel Import
- Configurable column mapping
- Data cleaning
- Validation pipeline

### Phase 2

- Spending analytics
- Budget tracking
- Vendor statistics
- Category insights

### Phase 3

- Interactive dashboard
- Charts & visualizations
- Export reports

### Phase 4

- LLM-powered natural language query interface
- Ask questions like:
  - "How much did I spend on food this month?"
  - "Show my top 10 merchants."
  - "Compare this month's spending with last month."

---

## Engineering Principles

This project follows several software engineering principles:

- Modular architecture
- Separation of concerns
- Single Responsibility Principle (SRP)
- Database normalization
- Atomic database transactions
- Configuration-driven design
- Integration testing

---

## Future Improvements

- LLM-powered natural language querying
- RAG-based financial assistant
- PostgreSQL migration
- Multi-user support
- Authentication
- OCR support for scanned statements
- PDF statement import
- Automated vendor classification
- Web application

---

## Author

**Piyush Kumar**

- GitHub: <https://github.com/piyush-k06>
- LinkedIn: <https://www.linkedin.com/in/piyush--kumar06/>

---
