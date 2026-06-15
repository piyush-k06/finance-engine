import sqlite3

con = sqlite3.connect('finance.db')
cur = con.cursor()

cur.execute('SELECT * FROM categories')

for x in cur.fetchall():
    print(x)

con.close()