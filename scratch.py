# from db import get_db
# con, cur = get_db()


# comment: checking foreign key

# cur.execute("PRAGMA table_info(vendor_aliases)")
# print(cur.fetchall())

# cur.execute("PRAGMA foreign_key_list(vendor_aliases)")
# print(cur.fetchall())




'''
Your task

Write the SQL yourself.

Requirements
alias_id → Primary Key
raw_name → TEXT, UNIQUE
vendor_id → Foreign Key → vendors.vendor_id
'''


# from db import get_db
# con, cur = get_db()

# cur.execute('''
# CREATE TABLE IF NOT EXISTS vendor_aliases(
#     alias_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     raw_name TEXT UNIQUE NOT NULL,
#     vendor_id INTEGER,
#     FOREIGN KEY(vendor_id) REFERENCES vendors(vendor_id)
# )
# ''')

# con.commit()
# con.close()


# testing vendor.py
from vendor import get_vendor_id

print(get_vendor_id("AMZN"))
print(get_vendor_id("AMZN"))
print(get_vendor_id("SWIGGY"))
print(get_vendor_id("SWIGGY"))