import pandas as pd
from openpyxl import load_workbook

# creare un database
dati = {
    'Nomi': ['Sarah', 'Pietro', 'John', 'Miriam', 'Zelda'],
    'Età': [26, 21, 25, 24, 22],
    'Città': ['Roma', 'Milano', 'Padova', 'Sicilia', 'Catania']
}

# DataFrame
df = pd.DataFrame(dati)
print(df)

# Salavare i dati in un file xlsx
df.to_excel('database.xlsx', index=False)

print("____________________________________________")
# Leggere il file xlsx
leggi_file = pd.read_excel('database.xlsx')
print(leggi_file)

print("____________________________________________")
# Ordinare i dati
dati_ord = df.sort_values(by='Età')
print(dati_ord)
dati_ord.to_excel("database.xlsx", index=False)





