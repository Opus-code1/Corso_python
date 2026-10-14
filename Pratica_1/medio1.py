# === PARTICA MEDIA 1 === #

'''
• Creare una variabile tipo str() di una domanda che chiede
    "piove fuori?"
• Creare una variabile di tipo str() che risponde con "si" o con "no"
• Verificare se la rosposta è "no"
    • Stampare usanto la funzione print() → "puoi uscire fuori"

• Verificare se la risposta è "si"
    • Crea una varibile domanda str() che chiede "Hai l'ombrello?"
    • Crea una varibile risposta str() che risponde con "si" o con "no"
    • Verificare se la risposta è "si"
        • Stampare usanto la funzione print() → "Puoi uscire fuori"
    • Verificare se la risposta è "no"
        • Stampare usanto la funzione print() → "Resta a casa"
'''
domanda1 = "fuori piove?"
domanda2 = "Hai l'ombrello?"
risposta1 = "si"
risposta2 = "no"

print(domanda1)
# fuori non sta piovendo
if risposta1 == "no":
    print('puoi uscire fuori')

# fuori sta piovendo → nel caso la risposta è "si"
else:
    print(domanda2)
    # si ho l'ombrello
    if risposta2 == "si":
        print("puoi uscire fuori")
    # no, non ho l'ombrello
    else:
        print("Non puoi uscire")

