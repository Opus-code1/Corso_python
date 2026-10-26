import pandas as pd
import numpy as np

def s(l=60):
    print("_" * l)

ordini = pd.read_csv('ordini.csv')
clienti = pd.read_csv('clienti.csv', sep=";")
prodotti = pd.read_csv('prodotti.csv')

s()
print(ordini.shape, clienti.shape, prodotti.shape)
s()


print(ordini.dtypes)
s()

print(ordini.isna().sum())
s()

print(ordini.head())
s()

