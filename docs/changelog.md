# Changelog

## 7 July 2026

### Added

- Vendor alias table
- Vendor management module
- Category lookup module
- Transaction insertion module
- Integration test module (`test_integration.py`)
- Database reset script (`scripts/reset_db.py`)
- Project documentation (`docs/`)

### Refactored

- Removed commit ownership from vendor module
- Transaction module now owns database commits
- Database connection ownership moved to `transaction.py`
- Vendor and category modules now use the caller's cursor instead of creating their own connections

### Fixed

- Fixed `sqlite3.OperationalError: database is locked` by using a single database connection
- Fixed module import side effect by removing executable test code from `transaction.py`

### Tested

- Existing vendor transaction insertion
- New vendor transaction insertion
- Invalid category handling
- Duplicate transaction behavior (expected for MVP)
- Vendor alias resolution
- End-to-end transaction pipeline

### Lessons Learned

- A single logical transaction should have only one commit owner.
- Avoid executable code at the module level; use test files or `if __name__ == "__main__":`.
- Integration testing is essential before adding new features.