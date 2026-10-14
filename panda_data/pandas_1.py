# === PANDAS === #
'pip install pandas'
def s(l=70):
    print("▄" * l)

dati = {
    'Prodotto': ['Mela', 'Pesca', 'Uva', 'Kiwi', 'Anguria'],
    'Prezzo': [2.25, 1.55, 2.99, 2.99, 5.68],
    'quant': [15,28,254,6,85]
}
s()
print(dati)
s()

# ========================================= #
import pandas as pd

df = pd.DataFrame(dati)

print(df)
s()
prezzi = df['Prezzo']
print(dati['Prezzo'])
s()
print(prezzi)
s()

