import os
import shutil

def sposta_file(origine, destinazione):
    # Verifica se la cartella di origine esiste
    if not os.path.exists(origine):
        print(f"La cartella {origine} non esiste.")
        return

    # Verifica se la cartella di destinazione esiste, altrimenti creala
    if not os.path.exists(destinazione):
        os.makedirs(destinazione)

    # Ottieni la lista dei file nella cartella di origine
    files = os.listdir(origine)

    # Sposta ciascun file nella cartella di destinazione
    for file in files:
        origine_file = os.path.join(origine, file)
        destinazione_file = os.path.join(destinazione, file)
        shutil.move(origine_file, destinazione_file)

# Esempio di utilizzo
cartella_origine = input("Inserisci il percorso della cartella di origine: ")
cartella_destinazione = input("Inserisci il percorso della cartella di destinazione: ")

sposta_file(cartella_origine, cartella_destinazione)
print("Spostamento completato.")
