# Mistakes

## 7 July 2026

### Mistake

Committed inside vendor.py.

Why it was wrong

Created multiple commits inside one logical transaction.

Lesson

Only the owner of the business operation should commit.

---

### Mistake

Created multiple database connections.

Error

sqlite3.OperationalError: database is locked

Solution

Pass cursor between modules.

Lesson

One transaction should use one connection.