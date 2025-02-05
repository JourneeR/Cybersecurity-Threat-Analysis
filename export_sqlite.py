import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("cybersecurity.db")

# Define queries
queries = {
    "login_attempts": "SELECT * FROM login_attempts;",
    "network_traffic": "SELECT * FROM network_traffic;",
    "cyber_alerts": "SELECT * FROM cyber_alerts;"
}

# Export each table to CSV
for table, query in queries.items():
    df = pd.read_sql_query(query, conn)
    df.to_csv(f"data/cybersecurity_processed_data/{table}.csv", index=False)

conn.close()
print("Data exported successfully!")
