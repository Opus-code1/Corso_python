'''
Scrivi un programma che chieda all'utente 
una stringa composta da un solo carattere 
e dica se si tratta di una vocale oppure no.
'''
vocali = "aeiou"
carattere = input("inserisci una sola lettera: ")

if carattere in vocali and not len(carattere) > 1:
    print("il carattere è una vocale")
elif carattere not in vocali and not len(carattere) > 1:
    print("il carattere non è una vocale")
else:
    print("carattere non valido")