import random, time

# inseriamo un numero da indovinare
numero = int(input("Numero: "))
t = 0
while True:
    casuale = random.randint(0, 100)
    print(casuale)
    time.sleep(0.001)
    if casuale == numero:
        print(f"il numero {numero} trovato in {t} tenattivi")
        break
    t += 1
    