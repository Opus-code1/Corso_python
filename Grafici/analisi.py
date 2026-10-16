import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

df = pd.read_csv('vendite.csv', parse_dates=['data'])

df = df.rename(columns={
    'città': 'citta',
    'quantità': 'quantita',
    'età_cliente': 'eta_cliente'})

df['mese'] = df['data'].dt.month
df['trimestre'] = df['data'].dt.quarter
df['giorno_settimana'] = df['data'].dt.day_name()


conteggio = df['tipo_di_cliente'].value_counts()
# print(conteggio)

fig, ax = plt.subplots(figsize=(7,7))

ax.pie(conteggio.values, autopct='%1.1f%%', startangle=90, 
    explode=[0.015,0.015,0.015], shadow=True)

fig.savefig("torta.png", dpi=150)
plt.show()