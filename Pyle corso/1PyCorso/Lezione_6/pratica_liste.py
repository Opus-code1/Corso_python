# abbiamo una lista spesa
spesa = []

# creiamo una variabile che chiede quanti prodotti vogliamo
num_prod = int(input("Quanti prodotti?\n->"))
# creiamo un cilo for
for i in range(num_prod):
    prodotto = input("Nome prodotto: ")
    spesa.append(prodotto)
    print(f"prodotti nella lista: {spesa}")
    
    



