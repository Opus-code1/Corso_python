import pandas as pd
def s(l=70): print("▄" * l)
file = './panda_data/vendite.csv'

s()
# stampa tutto (di default primi 5 dati e ultimi 5 dati per non intasare il pc)
df = pd.read_csv(file)
print(df)
s()

# stampa un numero di dati d anoi scelti "n=numero"
h = df.head(n=20)
print(h)

# stampa il totale di righe e colonne
s()
forma = df.shape
print(forma)

# solo colonne
s()
col = df.columns
print(col)

# tipo di ogni colonna
s()
dt = df.dtypes
print(dt)
s()

# informazioni complete
info1 = df.info()
print(info1)

s()
# stats
st = df.describe()

print(st)

'''
count → quanti valori "non-null" 
mean  → media (solo numerica)
std   → deviazione standard (quanto sono sparsi i  valore numerici)
min   → valore minimo
25%   → primo quartile
50%   → mediana
75%   → terzo quartile
max   → valore massimo

i valori mancati saranno NaN
'''

