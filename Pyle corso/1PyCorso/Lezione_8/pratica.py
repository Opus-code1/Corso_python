# dizionario vuoto
spesa = {}
# Chiave:Valore

# Ciclo WHILE per rendere il codice infinito
while True:
    print('______________________________________________________')
    # una variabile menu
    menu = input("1-Stampa\n2-Aggiungi\n3-Rimuovi\n4-Esci\n-> ")

    # condizioni 
    if menu == '1':
        # opzioni
        print('1-stampare tutto\n2-stampare prodotti\n3-stampare quantità\n4-stampare singolo prodotto')
        # una variabile per stampare
        stampa = input("-> ")
        if stampa == '1':
            print(spesa)
        elif stampa == '2':
            print(spesa.keys())
        elif stampa == '3':
            print(spesa.values())
        elif stampa == '4':
            prod = input("nome prodotto:")
            # se il prodotto è nel dizionario
            if prod in spesa:
                print(prod, spesa[prod])
            else:
                print(f'il {prod} non è nella lista!')
                continue
        
    elif menu == '2':
        q = input("numero prodotti -> ")
        # cilco FOR per aggiungere
        for i in range(int(q)):
            #diz[chiave] = valore
            #spesa[prodotto] = quant
            prod = input("nome prodotto: ")
            quant = input("Numero: ")
            spesa[prod] = quant
            print(spesa)
            
    elif menu == '3':
        q = int(input("numero prodotti: "))
        for i in range(q):
            print(spesa)
            rim = input("nome prodotto: ")
            if rim in spesa:
                del spesa[prod]
            else:
                pass

    elif menu == '4':
        print("ciao")
        break
    
    else:
        print("Errore")
        continue
            
            
            
