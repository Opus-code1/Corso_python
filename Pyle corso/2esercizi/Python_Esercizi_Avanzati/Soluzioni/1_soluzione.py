class Studente:
    def __init__(self, nome, cognome, voto):
        self.nome = nome
        self.cognome = cognome
        self.voto = voto

def aggiungi_studente():
    # Chiedi all'utente di inserire i dati dello studente
    nome = input("Inserisci il nome dello studente: ")
    cognome = input("Inserisci il cognome dello studente: ")
    voto = float(input("Inserisci il voto dello studente: "))

    # Crea un oggetto Studente
    studente = Studente(nome, cognome, voto)
    return studente

def salva_su_file(lista_studenti):
    with open("studenti.txt", "w") as file:
        for studente in lista_studenti:
            file.write(f"{studente.nome} {studente.cognome}: {studente.voto}\n")

# Esempio di utilizzo
lista_studenti = []

while True:
    print("\n1. Aggiungi studente\n2. Visualizza studenti\n3. Salva su file\n4. Esci")
    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        studente = aggiungi_studente()
        lista_studenti.append(studente)
    elif scelta == "2":
        for studente in lista_studenti:
            print(f"{studente.nome} {studente.cognome}: {studente.voto}")
    elif scelta == "3":
        salva_su_file(lista_studenti)
        print("Studenti salvati su file.")
    elif scelta == "4":
        break
    else:
        print("Scelta non valida. Riprova.")
