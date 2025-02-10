import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/cybersecurity_data/fake_login_attempts.csv")

sns.countplot(x="status", data=df)
plt.title("Successful vs Failed Login Attempts")
plt.show()
