giocattoli = {
    'palla':'un coso rotondo che rimbalza',
    'bambola': 'una persona in miniatura con cui giocare',
    }


ogg = giocattoli['palla']
#print(ogg)
#-----------------------------------------------------------
#         Chiave : Valore ,     Chiave : Valore
film = {'Titanic':'Dramma', 'mr. robot':'Scient...'}

titanic = "Dramma"
#print(titanic)
#print(film['Titanic'])
#-----------------------------------------------------------
# Manipolare i Dati

"""
clear() - Rimuove ogni dato dal dizionario
copy() - Restituisce una copia dei dati
fromkeys(keys, value) - Crea un nuovo dizionario con chiavi e valori impostati
get(key, default) - Restituisce il valore per key se key è nel dizionario 
items() - Restituisce una lista di oggetti che contiene una copia di chiave-valore
keys() - Restituisce tutte le cbiavi del dizionario
values() - Restituisce tutti i valori nel dizionario
pop() - Rimuove la chiave se esiste, se non esiste invece stampa un messaggio
popitem() - Rimuove e restituisce una copia di chaive-valore albitraria dal dizionario
"""

# ESEMPI
elimina = {'a':1, 'b':2, 'c':3}
print(f"Eliminare tutti i dati\nPrima:{elimina}")
elimina.clear()
print(f'Dopo:{elimina}')
print('__________________________________________________________')
print('Copia i valori')
original = {'a':1, 'b':2, 'c':3}

copia = original.copy()
print(copia)
print('__________________________________________________________')
print("Crea un Dizionario con i valori impostati")
chiavi = ['a', 'b', 'c']
valore = 0

il_dizionario = dict.fromkeys(chiavi, valore)
print(il_dizionario)
print('__________________________________________________________')
print('Metodo GET')

dizionario =  {'a':1, 'b':2}
print(dizionario.get('a'))
print(dizionario['b'])
print('Dato che non esiste')
print(dizionario.get('c'))
print('__________________________________________________________')
print('Metodo ITEMS')

oggetti =  {'a':1, 'b':2}
print(oggetti.items())
# dict_items([('a', 1), ('b', 2)])
# dict_items(  )
# [ ]
# ('a', 1), ('b', 2)
print('__________________________________________________________')
print('Metodo KEYS and VALUES')

numeri = {'John': '1568-6586', 'Sarah':'3954-5475'}
print(f"Tutti i dati: {numeri}\n")
print(f'Solo i nomi: {numeri.keys()}\n')
print(f'Solo i numeri:{numeri.values()}')
print('__________________________________________________________')
print('Metodo POP')

numeri = {'a': 1, 'b':2, 'c':'sarah'}
# if dato in dict delete and print(value) else print('Non esiste il dato)
valore_numeri = numeri.pop('c', 'Non esiste il dato')
print(valore_numeri)
print(numeri)
print('__________________________________________________________')
print('Metodo POPITEM')

dati = {'a': 1, 'b':2, 'c':3}
coppia = dati.popitem()
print(coppia)
print(dati)

print('__________________________________________________________')

studenti = {
    'Sarah':28,
    'Pietro':24,
    'Johnt':18,
    'Kaya':30
}
ultimo_studente = studenti.popitem()
print(f"Studente rimosso: {ultimo_studente}")
print(f"Studenti aggiornati: {studenti}")

print('__________________________________________________________')
print('Metodo DEL')
d = {
    1:2, 
    3:4, 
    5:6, 
    7:8
    }
print(d)
del d[7]
print(d)

print('__________________________________________________________')
print('Aggiungere i dati')
nomi = {}
nome = "Sarah"
nomi[nome] = 26
print(nomi)
print('__________________________________________________________')
print('Aggiornare i dati')

nome_dati = {"Miriam":25, "Zelda":27, "Pietro": 26}
print(nome_dati)
nome_dati['Pietro'] = 27
print(nome_dati)

print('__________________________________________________________')

d_1 = {}
key = input("Chiave:")
d_1[key] = input("Valore:")
print(d_1)

