'''
the spec for add_transaction() is now:
Accept date, raw_vendor, amount, category_name.
Get vendor_id.
Get category_id.
If category_id is None, raise an error.
Insert the transaction.
Commit.
Return transaction_id.
'''


from vendor import get_vendor_id
from category import get_category_id
from db import get_db
con, cur = get_db()

def add_transaction(date, raw_vendor, amount, category_name):
    vendor_id = get_vendor_id(cur, raw_vendor)
    category_id = get_category_id(cur, category_name)
    if category_id is None:
        raise ValueError("Category not found")
    cur.execute("INSERT INTO transactions(date, raw_vendor, vendor_id, amount, category_id) VALUES(?, ?, ?, ?, ?)", (date, raw_vendor, vendor_id, amount, category_id))
    con.commit()
    return cur.lastrowid


