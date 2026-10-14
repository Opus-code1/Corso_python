def conteggio_occorrenze(lista, elemento):
    contatore = lista.count(elemento)
    return contatore

# Esempio di utilizzo
lista_valori = [1, 2, 3, 4, 2, 5, 2, 6, 2, 7]
elemento_da_contare = 2
print(f"L'elemento {elemento_da_contare} compare {conteggio_occorrenze(lista_valori, elemento_da_contare)} volte nella lista.")
