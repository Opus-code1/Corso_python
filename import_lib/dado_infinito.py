import random
mi = 1
ma = 5
dado = random.randint(mi, ma)
tentativi = 3

while tentativi > 0:
    numero = int(input(f"numero da {mi} a {ma}: "))
    tentativi -= 1
    if numero == dado:
        print("Hai vinto")
        break
    else:
        # === aiuto === #
        if numero > dado:
            print("Il tuo numero è troppo alto")
        else:
            print("Il tuo numero è troppo basso")
        if tentativi > 1:
            print(f"Hai perso, hai ancora {tentativi} tentativi")
        elif tentativi == 1:
            print(f"Hai perso, hai ancora {tentativi} tentativo")
        else:
            print(f"Hai perso, non hai più i tentativi. Il numero era: {dado}")

