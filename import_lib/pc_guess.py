import random

numero = int(input("da 1 a 10.000: "))
tentativi = 0

while True:
    tentativi += 1
    indovina = random.randint(1, 10000)
    print(indovina)
    if indovina == numero:
        print(f"Ho indovinato il tuo numero in {tentativi} tentativi")
        continua = input("continuare? s/n: ")
        if continua == "n":
            break
        else:
            print("▄" * 30)
            num = int(input("da 1 a 10.000: "))
            numero = num