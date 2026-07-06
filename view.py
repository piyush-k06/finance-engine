import sqlite3
from db import get_db

con, cur = get_db()

cur.execute('SELECT * FROM categories')

for x in cur.fetchall():
    print(x)

con.close()