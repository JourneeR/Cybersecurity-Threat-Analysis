import pandas as pd
import random
import os
from faker import Faker

fake = Faker()

output_dir = "data/cybersecurity_data"
os.makedirs(output_dir, exist_ok=True)

#Generate fake cybersecurity alerts
alert_types = ['Extortion','Brute Force Attack', 'Malware Infection', 'Phishing Attempt', 'Insider Threats', 'DDoS Attack', 'Ransomware']
severities = ['low', 'medium', 'high', 'critical']

data = {
    "timestamp": pd.date_range(start="2024-01-01", periods=1000, freq="min"),
    "alert_type": [random.choice(alert_types) for _ in range(1000)],
    "source_ip": [fake.ipv4() for _ in range(1000)],
    "severity": [random.choice(severities) for _ in range(1000)],
}

df = pd.DataFrame(data)
print(df.head())  # Preview the first 5 rows
df.to_csv(f"{output_dir}/fake_cyber_alerts.csv", index=False)
print("Fake cybersecurity alerts dataset created successfully!")
