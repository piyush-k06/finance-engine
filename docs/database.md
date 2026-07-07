# Database Design

## Categories

Purpose:
Stores predefined spending categories.

Columns:

- category_id (PK)
- category_name

Notes:

Categories are fixed for MVP.

---

## Vendors

Purpose:

Stores canonical vendor names.

Columns:

- vendor_id (PK)
- vendor_name

---

## Vendor Aliases

Purpose:

Maps raw transaction names to canonical vendors.

Example:

AMZN -> Amazon

Columns:

- alias_id (PK)
- raw_name
- vendor_id (FK)

---

## Transactions

Purpose:

Stores all user transactions.

Columns:

- transaction_id (PK)
- date
- raw_vendor
- vendor_id (FK)
- amount
- category_id (FK)