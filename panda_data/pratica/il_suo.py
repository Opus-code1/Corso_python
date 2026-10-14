'''
Scrivi una 'funzione' che data in ingresso una 
lista A contenente n parole, restituisca 
in output una lista B di interi che rappresentano 
la lunghezza delle parole contenute in A.

Questo esercizio può essere risolto anche
usando una list comprehension.
'''

def parole(listA:list=[]):
    listB = []
    for i in listA:
        listB.append(len(i))
    return listB

print(parole(['ciao', 'ok', 'no', 'panda']))

# one line
def parole2(listA:list=[]): return [len(i) for i in listA]


print(parole2(['ciao', 'ok', 'no', 'panda']))