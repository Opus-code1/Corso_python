'''
una lista è una variabile che contiene zero o molti dati
al suo interno, i dati della lista possono essere qualsiasi
'''

# lista vuota
lista = []

# lista numeri
numeri = [1,22,3,4,5,3.14,0.5,9]

# lista stringhe
lettere = ['a','s','d','f','g']

# lista mista
mix = [1, 3.14, "panda", True, [2,3,5]]


spesa = []
print(f'lista della spesa: {spesa}')

# aggiungiamo un prodotto utilizzando append
print('\n')
print('spesa.append("Biscotti")')
spesa.append("Biscotti")
print(f'lista della spesa: {spesa}')
print('\n')
spesa.append("Uva")
spesa.append("Cereali")
spesa.append("Kiwi")
spesa.append("Kinder")
spesa.append("Monster")
spesa.append("Patatine")
spesa.append("Nutella")
print(f'lista della spesa: {spesa}')
print('\n')
# Rimuovo dalla lista usando remove
print('spesa.remove("Uva")')
spesa.remove("Uva")
print(f'lista della spesa: {spesa}')

print('\n')
# Rimuovo dalla lista usando pop
print('spesa.pop(2)')
spesa.pop(2)
print(f'lista della spesa: {spesa}')
print('\n')
# Svotare la lista con clear()
print('spesa.clear()')
spesa.clear()
print(f'lista della spesa: {spesa}')



