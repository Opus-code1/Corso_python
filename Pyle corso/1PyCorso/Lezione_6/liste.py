# INDICI DI UN LISTA
#           0        1       2
frutta = ['mele', 'pere', 'kiwi']
#          -3       -2      -1       

print(frutta[-3])
#-----------------------------------------------
# Metodo append aggiunge un dato alla fine della lista
frutta.append("mandarino")

print(frutta)

# Metodo insert aggiunge un dato in una posizione specifica
frutta.insert(1, 'uva')
print(frutta)
print("___________________________________________________________________________________________")
# Metodo Remove Eliminare i dati con il nome
menu = ['pizza', 'sushi', 'pesce', 'carne', 'pasta']
print(menu)

menu.remove('pesce')

print(menu)
# Metodo pop eliminare il dato senza conoscerlo, con indice
print("___________________________________________________________________________________________")
#          0        1        2        3        4        5        6
film = ['film 1','film 2','film 3','film 4','film 5','film 6','film 7']
print(film)

film.pop(4)
#     0         1          2        3          4        5 
# ['film 1', 'film 2', 'film 3', 'film 4', 'film 6', 'film 7']
print(film)

for titoli in film:
    film.pop(1)
print(film)
print("___________________________________________________________________________________________")

# metodo clear elimina tutti i dati dalla tua lista
numeri = [
    1,2,3,4,5,6,7,8,9,
    10,11,12,13,14,15,
    16,17,18,19,20,21
]
print(numeri)
numeri.clear()
print(numeri)

# Metodo reverse serve per capovolgere i dati delle liste
num = [1,2,3,4,5,6,7,8,9,10]

num.reverse()
print(num)

# Metodo sort ordina i dati 
dati = [5,8,9,64,7,65,2,324,89,21,32,58,2,5,85,6,8,70]
print('\n\n\n\n', dati)
dati.sort()
print(dati)

nomi = ["Sarah", "Pietro", 'Zelda', 'Zariel', "Antonio", 'Antonia', 'Roman', 'Miriam']

nomi.sort()
print(nomi)
print("___________________________________________________________________________________________")

#---------------------------------------------------------------------------
musica = ["Blanco", 'Annalisa', 'Geolier', "Neffex", "Lazza", "NF"]

# Metodo Slicing 
# dal indice 2 (il 2 è compreso) al indice 5 (5 non compr...)
print(musica[2:5])
# dal indici 0 (0 compr...) in poi (fino alla fine)
print(musica[0:])
# dal indice 5 (5 non compr...) al indice 0
print(musica[:5])


















