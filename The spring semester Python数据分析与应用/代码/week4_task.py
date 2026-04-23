import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("tripadvisor_review.csv")
plt.figure(figsize=(10,5))
sns.histplot(x=df["Category 1"],kde=True,color = 'red')
sns.histplot(y=df["User ID"],kde=False,color = 'blue')
plt.title("Users'advise for trip")
plt.ylabel("Nmuber")
plt.xlabel("Degree of satisfaction")
plt.show()