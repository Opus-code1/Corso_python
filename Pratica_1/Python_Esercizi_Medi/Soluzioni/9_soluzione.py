def lista_crescente(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1)

# Esempio di utilizzo
lista_crescente_test = [1, 2, 3, 4, 5]
print(f"La lista è crescente? {lista_crescente(lista_crescente_test)}")
