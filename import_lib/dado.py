# === LANCIO DEL DADO === #
import random

dado = random.randint(1, 6)

numero = int(input("Indovina il numero da 1 a 6: "))

if numero == dado:
    print(f"Hai vinto")
else:
    print(f"Hai perso! Il numero era {dado}")

