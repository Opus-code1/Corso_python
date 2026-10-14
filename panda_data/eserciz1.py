import pandas as pd
file = './panda_data/vendite.csv'
df = pd.read_csv(file)

print("=== PRIME RIGHE ===")
print(df.head())
print()

righe, colonne = df.shape

print(f"Righe: {righe}\nColonne: {colonne}")
print()

print(f"{df['Prezzo_Euro'].value_counts()}")
print()

