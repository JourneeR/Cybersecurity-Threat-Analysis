import sqlite3

# Create or connect to a database
conn = sqlite3.connect("cybersecurity.db")
cursor = conn.cursor()

print("Database connected successfully!")

# Close the connection
conn.close()

import sqlite3

# Connect to database
conn = sqlite3.connect("cybersecurity.db")
cursor = conn.cursor()

# Create Login Attempts Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS login_attempts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    user TEXT,
    ip_address TEXT,
    status TEXT
)
""")

# Create Network Traffic Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS network_traffic (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    source_ip TEXT,
    destination_ip TEXT,
    protocol TEXT,
    threat_level TEXT
)
""")

# Create Cybersecurity Alerts Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS cyber_alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    alert_type TEXT,
    source_ip TEXT,
    severity TEXT
)
""")

print("Tables created successfully!")

# Commit and close
conn.commit()
conn.close()
