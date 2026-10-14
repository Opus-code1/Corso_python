import menu

prezzi = []

def ordinazione():
    piatto = input("Primi o Bevande: ").lower()
    
    if piatto == 'primi':
        menu.primi()
        while True:
            ordine = input("Nome piatto: ")
            if ordine == "": break
            if ordine not in menu.primi_piatti: print(f"il piatto non è nel menù")
        # ===================================================================== #
            prezzi.append(menu.primi_piatti[ordine])
    if piatto == 'bevande':
        menu.bevande()
        while True:
            ordine = input("Nome bevanda: ")
            if ordine == "": break
            if ordine not in menu.bibite: print(f"il piatto non è nel menù")
        # ===================================================================== #
            prezzi.append(menu.bibite[ordine])
    conferma = input("conferma?\n: ").lower()
    if conferma == "si":
        totale = sum(prezzi)
        print(f"Totale: €{totale}")
    else:
        ordinazione()

if __name__ == "__main__":
    ordinazione()
