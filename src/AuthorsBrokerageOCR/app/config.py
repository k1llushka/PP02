import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")
DOCS_DIR = os.path.join(BASE_DIR, "documents")
TEMP_DIR = os.path.join(BASE_DIR, "temp")

DB_PATH = os.path.join(DATA_DIR, "system.db")

os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
