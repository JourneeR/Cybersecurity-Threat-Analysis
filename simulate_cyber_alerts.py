import pandas as pd
import random
import os
from faker import Faker

fake = Faker()

alert_types = ['Brute Force Attack', 'Malware Infection', 'Phishing Attempt', 'SQL Injection', 'DDoS Attack']
severities = ['low', 'medium', 'high', 'critical']

data = {
    "timestamp": pd.date_range(start="2024-01-01", periods=300, freq="min"),
    "alert_type": [random.choice(alert_types) for _ in range(300)],
    "source_ip": [fake.ipv4() for _ in range(300)],
    "severity": [random.choice(severities) for _ in range(300)],
}

df = pd.DataFrame(data)
print(df.head())  # Preview the first 5 rows

output_dir = "data/cybersecurity_data"
os.makedirs(output_dir, exist_ok=True)  # FIXED OSError

df.to_csv(f"{output_dir}/fake_cyber_alerts.csv", index=False)
print("Fake cybersecurity alerts dataset created successfully!")
