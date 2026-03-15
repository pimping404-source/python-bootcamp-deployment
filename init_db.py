import sqlite3
import pandas as pd
import os

# 1. Setup Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, 'business_ops.db')
CSV_PATH = os.path.join(BASE_DIR, 'data.csv')

def bootstrap_system():
    print("🚀 Starting Day 1: System Bootstrap...")
    
    # 2. Check if CSV exists
    if not os.path.exists(CSV_PATH):
        print(f"❌ Error: {CSV_PATH} not found. Create it first!")
        return

    # 3. Connect and Build Schema
    conn = sqlite3.connect(DB_PATH)
    try:
        # Load the CSV into a Pandas DataFrame
        df = pd.read_csv(CSV_PATH)
        
        # Save to SQLite (this creates the table 'inventory' automatically)
        df.to_sql('inventory', conn, if_exists='replace', index=False)
        
        # Create a separate 'sales' table to track revenue later
        conn.execute("""
            CREATE TABLE IF NOT EXISTS sales (
                sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
                item_name TEXT,
                amount REAL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        """)
        
        print(f"✅ Success! Database created at {DB_PATH}")
        print(f"📦 Imported {len(df)} items into 'inventory' table.")
        
    except Exception as e:
        print(f"🔥 Bootstrap Failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    bootstrap_system()