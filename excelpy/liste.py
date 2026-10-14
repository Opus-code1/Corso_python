'''
#            0       1       2       3        4
frutta = ['mela', 'pera', 'pesca', 'uva', 'fragole']
#           -5      -4      -3      -2       -1

print(frutta)

frutta[3]
print(frutta[3])


=== LISTE === 
x = 12 # variabile normale
lista_vuota = []
lista_numerica = [1,2,3,4,5,6,7,8,9]
lista_str = ['A','B','C','D']
lista_mista = [132, 3.14, "panda", True, x, lista_vuota, lista_numerica, [1,2,3,"a","b","c"], input(), print(), int()]

=== FORMAT LIST === 
one_line = [1,2,3,4,5,6]
multi_line = [1,2,3,
4,5,6]

personale = [
1,2,
    3,
    4,5,
        6,7,
    8,9,
            10,11,
                    12, 13
]
'''

# === MANIPOLAZIONE === #
colori = ['blu','rosso','verde']
print(colori)
# === AGGIUNGERE I DATI ALLA LISTA === à
'come = con append()'
'dove.append(cosa)'

colori.append('giallo') # ['blu','rosso','verde', 'giallo']
print(colori)
colori.append('grigio')
print(colori)
colori.append('rosso')
print(colori)
colori.append('viola')
print(colori)

# insert
'dove.insert(posizione, cosa)'
colori.insert(1, "ciano")
print(colori)

# === ELIMINARE I DATI DALLA LISTA === #
'da_dove.remove(cosa)'
colori.remove('grigio')
print(colori)
colori.remove('rosso')
print(colori)

'da_dove.pop()'
'da_dove.pop(posizione)'

# pop()
colori.pop()
print(colori)

# pop(posizione)
colori.pop(3)
print(colori)

print(colori.index('verde'))
print(colori.count('verde'))
