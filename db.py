import sqlite3

def get_db():
    con = sqlite3.connect("finance.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()
    return con, cur

