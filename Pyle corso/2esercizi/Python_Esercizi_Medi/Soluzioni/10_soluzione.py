class Libro:
    def __init__(self, titolo, autore, prezzo):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo

class NegozioLibri:
    def __init__(self):
        self.inventario = []

    def aggiungi_libro(self, libro):
        self.inventario.append(libro)

    def visualizza_inventario(self):
        for libro in self.inventario:
            print(f"{libro.titolo} di {libro.autore} - Prezzo: {libro.prezzo}€")

    def calcola_totale_stock(self):
        totale = sum(libro.prezzo for libro in self.inventario)
        return totale

# Esempio di utilizzo
libro1 = Libro("Il Signore degli Anelli", "J.R.R. Tolkien", 20)
libro2 = Libro("1984", "George Orwell", 15)

negozio = NegozioLibri()
negozio.aggiungi_libro(libro1)
negozio.aggiungi_libro(libro2)

print("Inventario del negozio:")
negozio.visualizza_inventario()

totale_stock = negozio.calcola_totale_stock()
print(f"\nTotale del valore degli stock nel negozio: {totale_stock}€")
