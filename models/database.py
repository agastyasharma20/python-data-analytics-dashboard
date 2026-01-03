import sqlite3

DB_NAME = "data.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            category TEXT NOT NULL,
            score INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()
