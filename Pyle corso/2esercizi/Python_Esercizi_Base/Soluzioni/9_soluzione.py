class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def descrizione(self):
        return f"{self.marca} {self.modello}"

auto = Veicolo("Toyota", "Corolla")
print("Descrizione dell'auto:", auto.descrizione())
