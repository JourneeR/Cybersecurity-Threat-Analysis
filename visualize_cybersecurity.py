import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to SQLite database
conn = sqlite3.connect("cybersecurity.db")

# Load Data
df_logins = pd.read_sql_query("SELECT * FROM login_attempts;", conn)
df_network = pd.read_sql_query("SELECT * FROM network_traffic;", conn)
df_alerts = pd.read_sql_query("SELECT * FROM cyber_alerts;", conn)

conn.close()

# Set Seaborn style
sns.set_theme(style="darkgrid")

# 1️⃣ Bar Chart: Failed vs Successful Logins
plt.figure(figsize=(8,5))
sns.countplot(x="status", hue="status", data=df_logins, palette="crest", legend=False)
plt.title("Login Attempt Status Distribution")
plt.xlabel("Login Status")
plt.ylabel("Count")
plt.show()

# 2️⃣ Line Chart: Network Attacks Over Time
df_network["timestamp"] = pd.to_datetime(df_network["timestamp"])
df_network["hour"] = df_network["timestamp"].dt.hour

plt.figure(figsize=(10,6))
sns.countplot(x="hour", hue="hour", data=df_network, palette="viridis", legend=False)
plt.title("Cyber Attacks by Hour")
plt.xlabel("Hour of the Day")
plt.ylabel("Attack Count")
plt.show()

# 3️⃣ Pie Chart: Threat Level Distribution
threat_counts = df_network["threat_level"].value_counts()
plt.figure(figsize=(6,6))
plt.pie(threat_counts, labels=threat_counts.index, autopct="%1.1f%%", colors=sns.color_palette("coolwarm", len(threat_counts)))
plt.title("Threat Level Distribution")
plt.show()
