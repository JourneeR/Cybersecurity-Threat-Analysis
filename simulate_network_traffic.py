import pandas as pd
import random
import os
from faker import Faker

fake = Faker()

# Generate 500 fake network traffic logs
protocols = ['TCP', 'UDP', 'ICMP', 'HTTP', 'HTTPS']
threat_levels = ['low', 'medium', 'high', 'critical']
source_ips = [fake.ipv4() for _ in range(50)]  # Generate 50 unique source IPs
dest_ips = [fake.ipv4() for _ in range(50)]    # Generate 50 unique destination IPs

data = {
    "timestamp": pd.date_range(start="2024-01-01", periods=500, freq="min"),
    "source_ip": [random.choice(source_ips) for _ in range(500)],
    "destination_ip": [random.choice(dest_ips) for _ in range(500)],
    "protocol": [random.choice(protocols) for _ in range(500)],
    "threat_level": [random.choice(threat_levels) for _ in range(500)],
}

df = pd.DataFrame(data)
print(df.head())  # Preview the first 5 rows

output_dir = "data/cybersecurity_data"
os.makedirs(output_dir, exist_ok=True)  # FIXED OSError

df.to_csv(f"{output_dir}/fake_network_traffic.csv", index=False)
# Save to CSV
print("Fake network traffic dataset created successfully!")
