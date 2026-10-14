# === LANCIO DELLA MONETA === #
import random
s = "▀" * 20

print(s)
print("=== METODO I ===")
# === METODO I === #
moneta = random.randint(0, 1)
# print(moneta) # DEBUG
scelta = input("Testa o Croce?\n→ ").lower()

if scelta == "croce" and moneta == 0:
    print("Hai vinto")
elif scelta == "testa" and moneta == 1:
    print("Hai vinto")
else:
    print("Hai perso")

print(s)
print("=== METODO II ===")
# === METODO II === #

moneta = random.choice("tc")
print(moneta) # DEBUG

scelta = input("Testa o Croce?\n→ ").lower()

if scelta == "testa" and moneta == "t":
    print("Hai vinto")
elif scelta == "croce" and moneta == "c":
    print("Hai vinto")
else:
    print("Hai perso")

# === METODO III === #
print(s)
print("=== METODO III ===")

moneta = ['testa', 'croce']
lancio = random.choice(moneta)

scelta = input("Testa o Croce?\n→ ").lower()

if scelta == lancio:
    print("Hai vinto!")
else:
    print("Hai perso!")

'''
# === USA E GETTA === #
if input("Testa o Croce?\n→ ").lower() == random.choice(['testa', 'croce']):
    print("Hai vinto!")
else:
    print("Hai perso!")
'''
