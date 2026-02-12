import sqlite3
import os

DB = "data/system.db"

def init_db():
    os.makedirs("data", exist_ok=True)

    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY,
        filename TEXT,
        fio TEXT,
        passport TEXT,
        text TEXT,
        created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def save_document(filename, fio, passport, text):
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO documents(filename, fio, passport, text)
    VALUES (?, ?, ?, ?)
    """, (filename, fio, passport, text))

    conn.commit()
    conn.close()
