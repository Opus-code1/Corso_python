class ElaboratoreLista:
    def __init__(self, lista):
        self.lista = lista

    def calcola_somma(self):
        return sum(self.lista)

    def calcola_media(self):
        return sum(self.lista) / len(self.lista)

def salva_risultati(somma, media):
    with open("risultati.txt", "w") as file:
        file.write(f"Somma: {somma}\nMedia: {media}\n")

# Esempio di utilizzo
lista_numeri = [float(x) for x in input("Inserisci una lista di numeri separati da spazi: ").split()]
elaboratore = ElaboratoreLista(lista_numeri)

somma = elaboratore.calcola_somma()
media = elaboratore.calcola_media()

salva_risultati(somma, media)
print("Risultati salvati su file.")
