import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="darkgrid", palette="Set2")

plt.rcParams["figure.figsize"] = (12, 7)


df =  pd.read_csv("vendite.csv")
df['data'] = pd.to_datetime(df["data"], format="%Y-%m-%d")
df['mese'] = df["data"].dt.month
df['trimestre'] = df["data"].dt.quarter

df['ricavo'] = df['totale_scontato']

df.head()

# === BARPLOT === #
# sns.barplot(data=df, x="categoria", y='ricavo', estimator="sum", color="blue")

# === LINEPLOT === #
# mensile = df.groupby('mese', as_index=False)['ricavo'].sum()
# sns.lineplot(data=mensile, marker='o')

# === BOXPLOT === #
sns.boxplot(data=df)


plt.show()
