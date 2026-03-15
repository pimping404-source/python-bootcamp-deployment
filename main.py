from fastapi import FastAPI
import sqlite3
import pandas as pd

app = FastAPI()

def get_db_connection():
    # Points to the DB your init_db.py just created
    conn = sqlite3.connect('business_ops.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get("/")
def read_root():
    return {"status": "API is Live", "database": "business_ops.db"}

@app.get("/inventory")
def get_inventory():
    conn = get_db_connection()
    # Querying the table created from your data.csv
    inventory = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return [dict(ix) for ix in inventory]