'''
Scrivi un programma che a partire da un 
elemento e una lista di elementi dica in 
output se l'elemento passato sia presente 
o meno nella lista.

Qualora l'elemento sia presente nella lista, il 
programma dovrà comunicarci l'indice dell'elemento 
tramite il metodo index.
'''
lista = ['a', 'b', 'c', 'd']

elem = "e"

if elem in lista:
    print(f'"{elem}" è presente in "{lista}" e ha indice {lista.index(elem)}')
else:
    print(f'"{elem}" nonè nella lista "{lista}"')

