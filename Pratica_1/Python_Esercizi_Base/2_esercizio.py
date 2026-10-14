'''
---Condizioni---

Modifica il programma precedente (ovvero la somma delle varibili) 
per includere una condizione.
Stampa "La somma è maggiore di 10" solo se la somma è 
effettivamente maggiore di 10.
'''
#---Inizio Codice---
numero_1 = 7.1452658
numero_2 = 3.5689

somma = numero_1 + numero_2

print(f"{numero_1} + {numero_2} = {somma}")

if somma > 10:
    print(f"il numero {somma} è maggiore di 10")