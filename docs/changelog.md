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


## 25 July 2026

### Added

- Configurable file import pipeline
- CSV and Excel file loading
- Configurable column mapping system
- Data cleaning pipeline
- Data validation pipeline
- Temporary transaction categorization module
- Transaction import pipeline
- Duplicate transaction handling

### Improved

- Standardized duplicate handling options (`skip`, `cancel`, `import_all`)
- Improved data cleaning for mixed CSV/Excel data types using Pandas `string` dtype

### Tested

- End-to-end import pipeline


## 2 August 2026

### Added

- Financial analytics module (`analytics.py`)
- Total spending calculation
- Category-wise spending summary
- Vendor-wise spending summary
- Monthly spending summary
- Highest transaction analysis
- Average transaction calculation

### Improved

- Updated project roadmap to reflect analytics progress
- Updated README with analytics module and current project status

### Tested

- Verified total spending calculation
- Verified category-wise spending summary
- Verified vendor-wise spending summary
- Verified monthly spending summary
- Verified highest transaction detection
- Verified average transaction calculation

### Lessons Learned

- Analytics functions should operate on DataFrames rather than directly querying the database.
- Avoid modifying input DataFrames; work on a copy when transformations are required.
- Keep analytics independent of the database layer to improve modularity and testability.