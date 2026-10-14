class Oggetto:
    def __init__(self, nome, descrizione):
        self.nome = nome
        self.descrizione = descrizione

def aggiungi_oggetto():
    nome = input("Inserisci il nome dell'oggetto: ")
    descrizione = input("Inserisci la descrizione dell'oggetto: ")

    oggetto = Oggetto(nome, descrizione)
    return oggetto

def salva_oggetti_su_file(lista_oggetti):
    with open("oggetti.txt", "w") as file:
        for oggetto in lista_oggetti:
            file.write(f"{oggetto.nome}: {oggetto.descrizione}\n")

# Esempio di utilizzo
lista_oggetti = []

while True:
    print("\n1. Aggiungi oggetto\n2. Visualizza oggetti\n3. Salva su file\n4. Esci")
    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        oggetto = aggiungi_oggetto()
        lista_oggetti.append(oggetto)
    elif scelta == "2":
        for oggetto in lista_oggetti:
            print(f"{oggetto.nome}: {oggetto.descrizione}")
    elif scelta == "3":
        salva_oggetti_su_file(lista_oggetti)
        print("Oggetti salvati su file.")
    elif scelta == "4":
        break
    else:
        print("Scelta non valida. Riprova.")
