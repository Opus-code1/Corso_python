'''
Scrivi un programma che chieda due numeri all'utente 
tramite la funzione input e mostri il più 
grande tra i due utilizzando la funzione print.
Per quanto Python disponga di una funzione max(), siete 
invitati ad utilizzare le istruzioni istruzioni 
if, elif ed else per la scrittura dell'algoritmo.
'''
num1 = int(input("inserisci il primo numero: "))
num2 = int(input("inserisci il secondo numero: "))

if num1 > num2: print(f"{num1} è il numero più grande.")

elif num1 < num2: print(f"{num2} è il numero più grande.")

else: print("i due numeri sono pari.")