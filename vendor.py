from db import get_db
con, cur = get_db()

def find_alias(raw_name):
    cur.execute("SELECT vendor_id FROM vendor_aliases WHERE raw_name=?", (raw_name,))
    vendor_id = cur.fetchone()
    return vendor_id[0] if vendor_id else None

def get_or_create_vendor(vendor_name):
    cur.execute("SELECT vendor_id FROM vendors WHERE vendor_name=?", (vendor_name,))
    vendor_id = cur.fetchone()
    if vendor_id: 
        return vendor_id[0]
    cur.execute("INSERT INTO vendors(vendor_name) VALUES(?)", (vendor_name,))
    return cur.lastrowid

def add_alias(raw_name, vendor_id):
    cur.execute("INSERT INTO vendor_aliases(raw_name, vendor_id) VALUES(?, ?)", (raw_name, vendor_id))
    
def get_vendor_id(raw_name, vendor_name=None):
    vendor_id = find_alias(raw_name)
    if vendor_id: 
        return vendor_id
    canonical_vendor_name = vendor_name or raw_name
    vendor_id = get_or_create_vendor(canonical_vendor_name)
    add_alias(raw_name, vendor_id)
    con.commit()
    return vendor_id