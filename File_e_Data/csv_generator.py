import random
import pandas as pd
from datetime import datetime, timedelta

# === ORDINI CSV === #
random.seed(42)

date_format = ['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y', '%d-%m-%Y']
righe = []

for i in range(300):
    data = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 364))
    fmt = random.choice(date_format)
    
    importo = random.choice([
        f'€{random.uniform(10, 500):.2f}',
        f'{random.uniform(10, 500):.2f}',
        f'€ {random.uniform(10, 500):.2f}',
        '' # dato mancante
    ])
    
    righe.append({
        'id_ordine': i + 1,
        'data': data.strftime(fmt),
        'id_cliente': random.choice([1,2,3,4,5,6,7,8,9,10,None]),
        'id_prodotto': random.choice([101,102,103,104,105,None]),
        'importo': importo,
        'quantita': random.choice([1,1,2,3,None,5])
    })
    
pd.DataFrame(righe).to_csv('ordini.csv', index=False, encoding='utf-8')
    
# === CLIENTI CSV === #
clienti = pd.DataFrame({
    'id_cliente': [1,2,3,4,5,6,7,8,9,10,2], # duplicato
    'nome': ['Marco', 'Giulia', 'Andrea', 
            'Sarah', 'Luca', 'Pietro', 'Antonio',
            'Rossi', 'Verdi', 'Giulio', 'Aelxandro'],
    'citta': ['Milano','milano','ROMA','Roma','Torino','torino',
            'Napoli','Napoli','Firenze','','Milano'],
    'email': ['a@x.it','b@x.it',None,'d@x.it','e@x.it',
            None,'g@x.it','h@x.it','i@x.it','j@x.it','b@x.it'],
})
clienti.to_csv('clienti.csv', index=False, sep=';', encoding='utf-8')

# === PRODOTTI CSV === #
prodotti = pd.DataFrame({
    'id_prodotto': [101,102,103,104,105],
    'nome_prodotto': ['Laptop', 'Mouse', 'Tastiera', 'Monitor', 'Cuffie'],
    'categoria': ['Elettronica', 'Accessori', 'Accessori', 'Elettronica', 'Audio'],
    'prezzo_listino': [999.0,25.0,79.0,349.0,129.0],
})

prodotti.to_csv('prodotti.csv', index=False, encoding='utf-8')

