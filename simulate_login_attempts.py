import pandas as pd
import random
import os
from faker import Faker

fake = Faker()

# Generate fake login attempts
users = ['admin', 'user1', 'user2', 'guest', 'root']
statuses = ['success', 'failed']
ips = [fake.ipv4() for _ in range(100)]  # Generate 100 unique IPs

data = {
    "timestamp": pd.date_range(start="2024-01-01", periods=500, freq="min"),  # FIXED WARNING
    "user": [random.choice(users) for _ in range(500)],
    "ip_address": [random.choice(ips) for _ in range(500)],
    "status": [random.choice(statuses) for _ in range(500)],
}

df = pd.DataFrame(data)
print(df.head())  # Preview the first 5 rows

# Ensure the directory exists before saving
output_dir = "data/cybersecurity_data"
os.makedirs(output_dir, exist_ok=True)  # FIXED OSError

df.to_csv(f"{output_dir}/fake_login_attempts.csv", index=False)
print("Fake login attempts dataset created successfully!")

