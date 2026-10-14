# CLASSI
# elementi chiavi di una classe
'''
- Classe è il modello da cui vengono creati gli oggetti
- Oggetto è un'istanza della classe
- Attributi sono le proprità che descrivono l'oggetto
- Metodi sono delle funzioni dentro una classe che descrivono il comportamento dell'oggetto
'''

# Creiamo una classe Cane
class Cane:
    # D-under function -> double under function
    def __init__(self, nome, razza):
        self.nome = nome
        self.razza = razza
        
    def abbaia(self):
        print(f'{self.nome} sta abbaiando!')
        
primo_cane = Cane("Stella", "Husky Siberiano")

print(f'{primo_cane.nome} è di razza {primo_cane.razza}')
primo_cane.abbaia()

second_cane = Cane("Sandra", "Labrador")

print(f'{second_cane.nome} è di razza {second_cane.razza}')
print('______________________________________________________')
'''
Cane: è la Classe
primo_cane: è un oggetto
nome e razza: sono attributi dell'oggetto
abbaia: è un metodo che descrive il comportamento dell'oggetto
'''

# forno che cucina i biscotti
class Biscotti:
    # forma
    def __init__(self, forma, numero) -> None:
        self.forma = forma
        self.numero = numero

# la prima ifornata pronta
prima_inf = Biscotti("Stella", 10)

# risultato
print(f'Ho fatto {prima_inf.numero} biscotti a forma di {prima_inf.forma}')

#----------------------------------------------------------------------------

class Valigia:
    def __init__(self, colore, dimensione) -> None:
        self.colore = colore
        self.dimensione = dimensione

prima_val = Valigia("Rosa", "Grande")
print(f'La mia valigia è {prima_val.colore} ed è {prima_val.dimensione}')


