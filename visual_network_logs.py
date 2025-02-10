import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/cybersecurity_data/fake_network_traffic.csv")

sns.countplot(x="threat_level", hue='threat_level', data=df, palette="viridis", legend=False)
plt.title("Threat Levels in Network Traffic")
plt.show()
