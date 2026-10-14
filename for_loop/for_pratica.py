# Traccia livello 4/5 - Ciclo for
# Obiettivo: usa il ciclo for per elaborare dati in liste e stringhe.
# Regole:
# - non usare dizionari, classi, tuple, funzioni
# - usa solo liste, stringhe, numeri e condizioni
# - usa almeno un ciclo for annidato

# Esercizio:
# Hai una lista di prodotti con i relativi prezzi e una lista di categorie.
# Scrivi un programma che:
# 1. stampa tutti i prodotti con prezzo superiore a 50
# 2. conta quanti prodotti hanno prezzo pari o superiore a 100
# 3. calcola il totale della spesa
# 4. trova il prodotto più costoso
# 5. stampa il nome di tutti i prodotti della categoria "Gaming"
# 6. stampa la media dei prezzi

# Lista dei nomi dei prodotti disponibili.
prodotti = ['Mouse', 'Tastiera', 'Monitor', 'Cuffie', 'Sedia', 'Webcam', 'Microfono']
# Lista dei prezzi associati a ciascun prodotto, nello stesso ordine di prodotti.
prezzi = [25, 45, 100,  50, 86, 47, 130]
# Lista delle categorie di appartenenza di ciascun prodotto.
categorie = ['Gaming','Ufficio','Gaming','Gaming','Ufficio','Ufficio','Gaming']

# 1) Stampa tutti i prodotti con prezzo superiore a 50.
# Itera su ogni indice della lista prodotti.
for i in range(len(prodotti)):
    # Se il prezzo del prodotto corrente è maggiore di 50, lo stampa.
    if prezzi[i] > 50:
        print(f"• {prodotti[i]}: €{prezzi[i]}")

# 2) Conta quanti prodotti hanno prezzo pari o superiore a 100.
# Inizia il contatore da zero.
contatore_costi = 0
# Esamina ogni singolo prezzo nella lista.
for prezzo in prezzi:
    # Se il prezzo è maggiore o uguale a 100, incrementa il contatore.
    if prezzo >= 100:
        contatore_costi += 1
# Stampa il totale dei prodotti costosi.
print(f"Prodotti superiori o uguali a €100 sono {contatore_costi}")

# 3) Calcola il totale della spesa.
# Variabile che accumula la somma totale dei prezzi.
totale = 0
# Somma ogni prezzo della lista.
for prezzo in prezzi:
    totale += prezzo
# Mostra il totale complessivo.
print(f"Totale: €{totale}")

# Totale II
# print(f"Totale: €{sum(prezzi)}")

# 4) Trova il prodotto più costoso.
# Inizializza il prezzo massimo con il primo elemento della lista.
max_prezzo = prezzi[0]
# Inizializza il nome del prodotto più costoso con il primo prodotto.
max_prod = prodotti[0]

# Scorre tutti gli indici per confrontare i prezzi.
for i in range(len(prodotti)):
    # Se il prezzo corrente è maggiore del massimo trovato finora,
    # aggiorna il massimo e il prodotto corrispondente.
    if prezzi[i] > max_prezzo:
        max_prezzo = prezzi[i]
        max_prod = prodotti[i]

# Stampa il prodotto e il prezzo massimo.
print(f"Prodotto più costoso: {max_prod} che costa €{max_prezzo}")

# 5) Stampa il nome di tutti i prodotti della categoria "Gaming".
# Ciclo annidato: per ogni prodotto, controlla tutte le categorie.
for i in range(len(prodotti)):
    for j in range(len(categorie)):
        # Verifica che gli indici coincidano e che la categoria sia "Gaming".
        if i == j and categorie[j] == "Gaming":
            print(f"• {prodotti[i]}")

# 6) Calcola la media dei prezzi.
# Somma tutti i prezzi per poi dividerli per il numero di elementi.
somma = 0
for prezzo in prezzi:
    somma += prezzo

# Divide la somma totale per il numero di prezzi.
media = somma / len(prezzi)
# Stampa la media dei prezzi.
print(f"Media dei prezzi: {media}")