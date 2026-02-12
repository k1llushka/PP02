import sqlite3
from datetime import datetime
from app.config import DB_PATH


def log(action: str):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        action TEXT,
        created_at TEXT
    )
    """)

    cur.execute(
        "INSERT INTO logs(action, created_at) VALUES (?, ?)",
        (action, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    )

    conn.commit()
    conn.close()
