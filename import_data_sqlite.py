import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("cybersecurity.db")
cursor = conn.cursor()

# Load Login Attempts Data
df_logins = pd.read_csv("data/cybersecurity_data/fake_login_attempts.csv")
df_logins.to_sql("login_attempts", conn, if_exists="append", index=False)

# Load Network Traffic Data
df_traffic = pd.read_csv("data/cybersecurity_data/fake_network_traffic.csv")
df_traffic.to_sql("network_traffic", conn, if_exists="append", index=False)

# Load Cyber Alerts Data
df_alerts = pd.read_csv("data/cybersecurity_data/fake_cyber_alerts.csv")
df_alerts.to_sql("cyber_alerts", conn, if_exists="append", index=False)

print("Data imported successfully!")

# Commit and close
import sqlite3
print(sqlite3.version)  # Shows SQLite module version
print(sqlite3.sqlite_version)  # Shows actual SQLite engine version

conn.close()
