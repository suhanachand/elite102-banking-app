import sqlite3
import os

DB_NAME = "bank.db"


def connect():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accounts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        balance REAL DEFAULT 0
    )
    """)

    conn.commit()
    conn.close()


def get_db_path():
    return os.path.abspath(DB_NAME)
