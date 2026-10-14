import random as r
import time
# === SNEZA FUNZIONI === #
'''
while True:
    moneta = input("Testa o Croce?\n: ").lower()

    if r.choice(['testa','croce']) == moneta:
        print("Hai vinto")

    else:
        print("Hai perso")
        continua = input("vuoi continuare?\n: ").lower()
        if continua == "no":
            break

dado = r.randint(1, 6)

numero = int(input("Numero da 1 a 6: "))
if numero == dado:
    print("hai vinto")
else:
    print('hai perso')
'''
# === CON LE FUNZIONI === #
def moneta():
    print("Hai vinto") if input("testa o croce: ").lower() == r.choice(['testa', 'croce']) else print('hai perso')

def dado():
    print("hai vinto") if int(input("numero da 1 a 6: ")) == r.randint(1,6) else print("hai perso")

def scf():
    # === SASSO - CARTA - FORBICI === #
    punti_gicatore = 0
    punti_computer = 0
    scelta_computer = ["sasso", "carta", "forbici"]
    s = "▀" * 30

    while True:
        time.sleep(0.5)
        print(s)
        # === GAME OVER === #
        if punti_gicatore >= 3 or punti_computer >= 3:
            if punti_gicatore > punti_computer:
                print("Hai vinto tu la partita")
            else:
                print("Hai perso la partita")
            break # blocca tutto
        # ==================================================================== #
        scelta_giocatore = input("Scegli tra Sasso - Carta - Forbici\n→ ").lower()
        computer = r.choice(scelta_computer)
        print(s)
        time.sleep(0.5)
        print(f'Il computer ha deciso di giocare con: "{computer}"')
        print(s)
        time.sleep(0.5)
        # === PARI === #
        if scelta_giocatore == computer:
            print("Siete Pari")
            print(s)
            time.sleep(0.5)
        # === VINCE IL GIOCATORE === #
        elif scelta_giocatore == 'sasso' and computer == "forbici":
            print(f"Hai vinto! +1 punto per te")
            punti_gicatore = punti_gicatore + 1 # punti_gicatore += 1
            print(f"Punti totali:\nGiocatore: {punti_gicatore}\nComputer: {punti_computer}")
            print(s)
            time.sleep(0.5)
        elif scelta_giocatore == "carta" and computer == "sasso":
            print(f"Hai vinto! +1 punto per te")
            punti_gicatore = punti_gicatore + 1 # punti_gicatore += 1
            print(f"Punti totali:\nGiocatore: {punti_gicatore}\nComputer: {punti_computer}")
            print(s)
            time.sleep(0.5)
        elif scelta_giocatore == "forbici" and computer == "carta":
            print(f"Hai vinto! +1 punto per te")
            punti_gicatore = punti_gicatore + 1 # punti_gicatore += 1
            print(f"Punti totali:\nGiocatore: {punti_gicatore}\nComputer: {punti_computer}")
            print(s)
            time.sleep(0.5)
        else:
            punti_computer += 1
            print(f"Hai perso! +1 punto al computer,")
            print(f"Punti totali:\nGiocatore: {punti_gicatore}\nComputer: {punti_computer}")
            print(s)
            time.sleep(0.5)

def main():
    giochi = input("home-moneta-dado-sasso, carta, forbici: ").lower()

    if giochi == "moneta": moneta()
    elif giochi == "dado": dado()
    elif giochi == "scf": scf()
    else: main()

from esempio2 import crea_file as cf

cf()
cf('esempio.py')
cf(nome="esempio.json")


