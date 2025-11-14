# scripts/ingest_to_sqlite.py
import sqlite3
import pandas as pd
import os

os.makedirs("data", exist_ok=True)
DB_PATH = "data/ecom.db"

def load_csv_to_table(conn, csv_path, table_name):
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {csv_path}")

def main():
    conn = sqlite3.connect(DB_PATH)
    load_csv_to_table(conn, "data/categories.csv", "categories")
    load_csv_to_table(conn, "data/products.csv", "products")
    load_csv_to_table(conn, "data/customers.csv", "customers")
    load_csv_to_table(conn, "data/orders.csv", "orders")
    load_csv_to_table(conn, "data/order_items.csv", "order_items")
    conn.commit()
    conn.close()
    print("Created SQLite DB at", DB_PATH)

if __name__ == "__main__":
    main()
