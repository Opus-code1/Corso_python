import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("./MatPlot/vendite.xlsx", sheet_name="Vendite")

print(df.head())
print(df.shape)
print(df.describe())

colori = [
    "#4bd21e",
    "#d8cd30",
    "#d85d30",
    "#30d8c2",
    "#304fd8",
    "#a330d8",
    "#d830ae",
    "#d8306e",
    "#d83030",
    "#4B4494"
]
top10 = df.nlargest(10, "Totale")
print(top10)

plt.figure(edgecolor="red", figsize=(12, 6), facecolor="white")

plt.barh(top10['Prodotto'], top10["Totale"], color=colori)
plt.title("Top 10 prodotti venduti questo mese")
plt.xlabel("TOTALE")
plt.gca().invert_xaxis()
plt.gca().invert_yaxis()
plt.grid(color="blue", linestyle="--", alpha=0.2)
plt.tight_layout()
plt.show()
