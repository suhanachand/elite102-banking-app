
import sqlite3

def connect():
    return sqlite3.connect("bank.db")

def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        balance REAL
    )
    """)

    conn.commit()
    conn.close()
