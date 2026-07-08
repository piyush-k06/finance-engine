from db import get_db

con, cur = get_db()

cur.execute("DELETE FROM transactions")
cur.execute("DELETE FROM vendor_aliases")
cur.execute("DELETE FROM vendors")

cur.execute("DELETE FROM sqlite_sequence WHERE name='transactions'")
cur.execute("DELETE FROM sqlite_sequence WHERE name='vendor_aliases'")
cur.execute("DELETE FROM sqlite_sequence WHERE name='vendors'")

con.commit()

con.close()

print("Database reset.")