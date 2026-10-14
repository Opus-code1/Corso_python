'''
Scrivi un semplice programma che, data 
una lista di numeri, sommi tra loro tutti gli elementi.

Suggerimento: anche se esiste 
la funzione sum() per risolvere 
l'esercizio potresti usare il ciclo for.
'''
numeri = [5,-9,85,78,-45,2,0,1,1,1,5,6,76]
x = 0

for i in numeri:
    print(f"{x} + {i} = {x + i}")
    x += i

print(f"La somma di tutti i numeri è {x}")

