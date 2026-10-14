import matplotlib as ml
import matplotlib.pyplot as plt

'''
-Grafico Lineare
-Grafico a Barre
-Grafico a Dispersione
-Grafico a Torta
-Grafico Personale
'''
# CREAIAMO UN GRAFICO
quant = [1, 2, 3, 4]
prezzo = [1, 6, 8, 2]
x = quant
y = prezzo
plt.plot(x, y, marker='o')

plt.title("Grafico Lineare")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")

plt.show()

'''
plt.plot(x, y) è un grafico lineare
plt.title() è un titolo
plt.xlabel è un titolo della x
plt.ylabel è un titolo della y
plt.show() è avvio del grafico
'''

categoria =  ['Scarpe', 'Borsa', 'Felpe', 'Giacche']
valore = [3, 7, 5, 8]

# creiamo un grafico a barre
plt.bar(categoria, valore, color = "pink")

plt.title("Grafico a Barre")
plt.xlabel("Categoria")
plt.ylabel("Valore")

plt.show()

# Grafico a dispersione

# Dati
x = [1,6,10,9,7,3,2,5,4,8]
y = [99,78,53,45,15,100,140,84,71,20]

plt.scatter(x, y, color = "purple")

plt.title("Grafico a Dispersione")
plt.xlabel("Asse X")
plt.ylabel("Asse Y")

plt.show()

# Grafico a Torta

frutta = ["mele", 'pesche', 'kiwi', 'arance']
quant = [15, 20, 5, 50]
plt.pie(quant, labels=frutta, autopct='%1.1f%%')
plt.show()

'''
%1.1f%% stringa di formattazione

%1.1f come formattare il numero

1.1 significa visualizza solo una cifra prima del punto decimale

f indica il float point
'''




