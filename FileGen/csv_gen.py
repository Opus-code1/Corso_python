# pip install python-csv #

import csv
import random

citta_regioni = [
    ('Milano', 'Lombardia'),
    ('Roma', 'Lazio'),
    ('Napoli', 'Campania'),
    ('Torino', 'Piemonte'),
    ('Palermo', 'Sicilia'),
    ('Genova', 'Liguria'),
    ('Bologna', 'Emilia-Romagna'),
    ('Firenze', 'Toscana'),
    ('Bari', 'Puglia'),
    ('Matera', 'Basilicata'),
    ('Venezia', 'Veneto'),
] 

categorie = ['Elettronica','Abbigliamento','Sport','Alimentari','Casa']

prodotti = {
    "Elettronica": ['Telefono', 'Laptop', 'Tablet', 'Cuffie', 'Microfono'],
    "Abbigliamento": ['Maglietta','Pantaloni','Giacca','Scarpe','Cappello'],
    "Sport": ['Panca','Manubi','Dischi','Zaino','Borraccia'],
    "Alimentari": ['Pasta','Olio','Pane','Farina','Caffè'],
    "Casa": ['Lampada','Tappeto','Piatti','Tavoli','Sedie']
}

prezzi = {
    "Elettronica": (50, 1600),
    "Abbigliamento": (15, 150),
    "Sport": (15, 600),
    "Alimentari": (3, 250),
    "Casa": (10, 800),
}

max_righe = 500

righe = []

for i in range(max_righe):
    mese = random.randint(1, 12)
    giorno = random.randint(1 ,28)
    data = f"2024-{mese}-{giorno}"
    
    citta, regione = random.choice(citta_regioni)
    categoria = random.choice(categorie)
    prodotto = random.choice(prodotti[categoria])
    
    prezzo_min, prezzo_max = prezzi[categoria]
    prezzo_unit = round(random.uniform(prezzo_min, prezzo_max), 2)
    
    quantita = random.randint(1, 8)
    totale = round(prezzo_unit * quantita, 2)
    
    # sconto del 20%
    sconto = round(random.uniform(0.05, 0.30), 2) if random.random() < 0.2 else 0.0
    totale_scontato = round(totale * (1 - sconto), 2)

    cliente = random.choice(['Nuovo', 'Fedele', 'VIP'])
    eta = random.randint(18, 75)
    pagamento = random.choice(['Carta','Contanti','Bonifico','PayPal'])
    
    righe.append({
        "data": data,
        "città": citta,
        "regione": regione,
        "categoria": categoria,
        "prodotto": prodotto,
        "prezzo_unitario": prezzo_unit,
        "quantità": quantita,
        "totale": totale,
        "sconto": sconto,
        "totale_scontato": totale_scontato,
        "tipo_di_cliente": cliente,
        "età_cliente": eta,
        "metodo_di_pagamento": pagamento
    })
    

with open("vendite.csv", "w", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=righe[0].keys())
    writer.writeheader()
    writer.writerows(righe)
    