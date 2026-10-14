# === PRATICA MEDIO 2 === #
'''
• Crea un variabile str() chiamata "temperatura" (opzionale)
• Verifica se la temperatura è minore o uguale a 20
    • Stampa usando la funzione print() "Fa freddo, vestiti bene"
• Verifica se la temperatura è maggiore di 20
    • Stampa usando la funzione print() "il clima è mite, vestiti"
• Verifica se la temperatura è maggiore o uguale a 32
    • Stampa usando la funzione print() "Fa caldo mettit un qualcosa sopra la testa"
'''
# === CODICE 1 === #
temp = int(input("inserisci i gradi: "))

if temp <= 20:
    print("Fa freddo, vestiti bene")

elif temp >= 32:
    print("Fa caldo mettiti un qualcosa sopra la testa")

else:
    print("il clima è mite, vestiti")
    
    
# === CODICE 2 === #
if temp <= 20:
    print("Fa freddo, vestiti bene")

elif temp > 20: # da 21 a 31
    if temp >= 32: # da 32 in poi
        print("Fa caldo mettiti un qualcosa sopra la testa")
    else:
        print("il clima è mite, vestiti")
    
#  === OPERATORI DI CONFRONTO === #
if temp <= 20:
    print("Fa freddo, vestiti bene")

elif temp >= 20 and temp < 32:
    print("il clima è mite, vestiti")
else:
    print("Fa caldo mettiti un qualcosa sopra la testa")

'''
or   → OPPURE → 5 > 2 or 6 < 5 or "ciao" == "ciao"
and  → E/ANCHE → password == "pswd123" and email == "mario@gmail.com"
in   → DENTRO → "a" in "ciao"
'''
