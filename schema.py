import sqlite3

con = sqlite3.connect('finance.db')
cur = con.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS vendors(
    vendor_id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_name TEXT UNIQUE
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS categories(
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT UNIQUE
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS transactions(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,

    date TEXT,

    raw_vendor TEXT,

    vendor_id INTEGER,

    amount REAL,

    category_id INTEGER,

    FOREIGN KEY(vendor_id)
    REFERENCES vendors(vendor_id),

    FOREIGN KEY(category_id)
    REFERENCES categories(category_id)
)
''')

cats = [
    'Food',
    'Travel',
    'Shopping',
    'Bills',
    'Subscription',
    'Income',
    'Healthcare',
    'Education',
    'Uncategorized'
]

for x in cats:
    cur.execute(
        'INSERT OR IGNORE INTO categories(category_name) VALUES(?)',
        (x,)
    )

con.commit()
con.close()

print('db created')