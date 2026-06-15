import sqlite3

con = sqlite3.connect('finance.db')
cur = con.cursor()

cur.execute(
    'INSERT OR IGNORE INTO vendors(vendor_name) VALUES(?)',
    ('Swiggy',)
)

cur.execute(
    'INSERT OR IGNORE INTO vendors(vendor_name) VALUES(?)',
    ('Netflix',)
)

cur.execute(
    'SELECT vendor_id FROM vendors WHERE vendor_name=?',
    ('Swiggy',)
)

v = cur.fetchone()[0]

cur.execute(
    'SELECT category_id FROM categories WHERE category_name=?',
    ('Food',)
)

c = cur.fetchone()[0]

cur.execute('''
INSERT INTO transactions(
date,
raw_vendor,
vendor_id,
amount,
category_id
)
VALUES(?,?,?,?,?)
''',
(
'2026-06-13',
'SWIGGY LTD',
v,
-350,
c
))



con.commit()
con.close()

print('done')