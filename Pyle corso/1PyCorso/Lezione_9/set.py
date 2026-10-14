# SET
# creazione di un SET
set_1 = {1,2,3,4,5,6}
set_2 = set()
# aggiungere un elemento al SET add()
set_3 = {1, 2, 3}
set_3.add(4)
print(set_3)
print('__________________________________________')
# rimuovere un elemento dal SET remove()
set_3.remove(3)
print(set_3)
print('__________________________________________')
# verifica se un dato è nel set
print(2 in set_3) # True
print(3 in set_3) # False
print('__________________________________________')
#-------------------------------------------
# unione di due o più set
s_1 = {1,2,3}
s_2 = {4,5,6}
s_3 = s_1 | s_2
print(s_3)
print('__________________________________________')
# intersezione di due o più set
inters = s_1 & s_2
print(inters)
print('__________________________________________')
# differenze dei due o più set
ds_1 = {1,2,3}
ds_2 = {4,5,6}
dif = ds_2 - ds_1
print(dif)
print('__________________________________________')
# update, aggiungere più elemneti in un SET
set1 = {1,2,3}
set1.update([4,5,6,7,8,9])
print(set1)
# rimuovere senza generare un errore con discard()
set2 = {1,2,3}
# set2.remove(4) # mi da un errore
set2.discard(4)
print(set2)
print('__________________________________________')
# differenza simmetrica
s1 = {1,2,3}
s2 = {2,3,5}
s3 = {1,6,3}
dif_sim = s1 ^ s2 ^ s3
print(dif_sim)
print('__________________________________________')
# unione con union()
st1 = {1,2,3}
st2 = {3,4,5}
st4 = {7,8,9}
st5 = {10,11,12}
st3 = st1.union(st2)#, st4.union(st5)
print(st3)
print('__________________________________________')
# intersection() Restituisce un nuovo set che contiene i dati comuni
st1 = {1,2,3}
st2 = {3,4,5}
inters = st1.intersection(st2)
print(inters)
print('__________________________________________')
# differense()
dif = st1.difference(st2)
print(dif)
print('__________________________________________')
lista = [1,2,3,4,5,6,7,8,9]
x = set(lista)
print(x)

'''
1-Unicità degli Elementi
2-Non ordinato
3-Mutabile
4-Elementi non Mutabili
'''

