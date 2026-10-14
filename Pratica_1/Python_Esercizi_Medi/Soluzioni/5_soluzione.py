def palindromo(parola):
    parola = parola.lower()
    return parola == parola[::-1]

# Esempio di utilizzo
parola_test = "radar"
print(f"La parola {parola_test} è palindroma? {palindromo(parola_test)}")
