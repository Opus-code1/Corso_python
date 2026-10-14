def conteggio_vocali(stringa):
    vocali = "aeiouAEIOU"
    contatore = 0
    for carattere in stringa:
        if carattere in vocali:
            contatore += 1
    return contatore

# Esempio di utilizzo
parola = "Python Programming"
print(f"Il numero di vocali nella stringa è {conteggio_vocali(parola)}")
