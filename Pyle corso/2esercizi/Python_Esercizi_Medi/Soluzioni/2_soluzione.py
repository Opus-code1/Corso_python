def calcola_fattoriale(n):
    risultato = 1
    while n > 0:
        risultato *= n
        n -= 1
    return risultato

# Esempio di utilizzo
numero = 5
print(f"Il fattoriale di {numero} è {calcola_fattoriale(numero)}")
