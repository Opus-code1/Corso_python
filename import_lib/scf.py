# === SASSO - CARTA - FORBICI === #
'''
Carta vince sul Sasso
Sasso Vince sulle Forbici
Forbici vincono slla Carta

• CHI lo userà
- 1 Persona
    ╚1 unamno vs computer
        ╚ computer → random

• COME funziona
    ╚ persona sceglie una mossa
        ╚ Computer sceglie una mossa
            ╚ Si decide chi ha vinto
                ╚ Vince chi arriva per primo a 3 punti
'''
import random
import time
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
    computer = random.choice(scelta_computer)
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
