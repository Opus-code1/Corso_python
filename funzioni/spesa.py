spesa = []
def s(lung=50, indchar=0, char=['▄','█','.',':','-','=']):
    print(char[indchar] * lung)

# === FUNZIONE AGGIUNGI ALLA LISTA === #
def aggiungi():
    quant = int(input("Numero di prodotti da aggiungere: "))
    
    for i in range(quant):
        prodotto = input("Nome prodotto: ")
        s()
        # --- se il prodotto è nella lista --- #
        while prodotto in spesa:
            print(f'il prodotto: "{prodotto}" è già nella lista, aggiungere lo stesso?')
            conferma = input(": ").lower()
            s()
            if conferma == 'si':
                spesa.append(prodotto)
                print(f'"{prodotto}" aggiunto nella lista!')
                break
            else:
                break
        else:
            spesa.append(prodotto)
            print(f'"{prodotto}" aggiunto nella lista!')
    main()

# === FUNIZONE RIMUOVI DALLA LISTA === #
def rimuovi():
    quant = int(input("quanti prodotti rimuovere: "))
    while quant > len(spesa) or quant < 0:
        print(f"non hai tutti questi prodotti nella lista\nhai {len(spesa)} prodotti in totale")
        quant = int(input("quanti prodotti rimuovere: "))
    # --------------------------------------------------------- #
    for i in range(quant):
        print("=== PRODOTTI DISPONIBILI ===")
        for p in spesa:
            print(f"• {p}")
        s()
        prodotto = input("Prodotto da rimuovere: ")
        while prodotto not in spesa:
            print(f'"{prodotto}" non è nella lista!')
            prodotto = input("Prodotto da rimuovere: ")
        else:
            spesa.remove(prodotto)
            print(f'"{prodotto}" è stato rimosso')
            s()
    main()

def main():
    s()
    scelta = input(f"1-Vedi lista\n2-Aggiungi alla lista\n3-Rimuovi dalla lista\n4-Elimina tutto\n5-Esci\n: ")
    while scelta not in ['1','2','3','4','5']:
        s()
        print("Scelta non valida!")
        scelta = input(f"1-Vedi lista\n2-Aggiungi alla lista\n3-Rimuovi dalla lista\n4-Elimina tutto\n5-Esci\n: ")
    if scelta == "1":
        # === MOSTRA LA LISTA === #
        print("=== PRODOTTI NELLA LISTA ===")
        for prodotti in spesa:
            print(f"• {prodotti}")
        if len(spesa) < 1:
            print("NESSUN PRODOTTO TOVATO NELLA LISTA")
        main()
    elif scelta == "2":
        aggiungi()
    elif scelta == "3":
        rimuovi()
    elif scelta == "4":
        if input("confermi?\n: ").lower() == "si": 
            spesa.clear()
            print("Prodotti eliminati dalla lista")
        main()
    elif scelta == "5":
        return
    # ============================================================ #

if __name__ == "__main__":
    main()
