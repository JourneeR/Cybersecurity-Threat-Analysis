import pandas as pd
import random
import os
from faker import Faker

fake = Faker()

# Ensure the directory exists before saving
output_dir = "data/cybersecurity_data"
os.makedirs(output_dir, exist_ok=True)

# Generate fake login attempts

users = ['admin', 'user1', 'user2', 'guest', 'root']
statuses = ['success', 'failed']
ips = [fake.ipv4() for _ in range(300)]  # Generate 300 unique IPs

data = {
    "timestamp": pd.date_range(start="2024-01-01", periods=1000, freq="min"),  # FIXED WARNING
    "user": [random.choice(users) for _ in range(1000)],
    "ip_address": [random.choice(ips) for _ in range(1000)],
    "status": [random.choice(statuses) for _ in range(1000)],
}

df = pd.DataFrame(data)
print(df.head())  # Preview the first 5 rows
df.to_csv(f"{output_dir}/fake_login_attempts.csv", index=False)
print("Fake login attempts dataset created successfully!")

