def ricerca_binaria(lista, elemento):
    inizio, fine = 0, len(lista) - 1
    while inizio <= fine:
        medio = (inizio + fine) // 2
        if lista[medio] == elemento:
            return True
        elif lista[medio] < elemento:
            inizio = medio + 1
        else:
            fine = medio - 1
    return False

# Esempio di utilizzo
lista_ordinata = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento_cercato = 8
print(f"L'elemento {elemento_cercato} è presente nella lista? {ricerca_binaria(lista_ordinata, elemento_cercato)}")
