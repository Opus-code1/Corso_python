import random
#-----------------------------------#

dado = random.randint(1,6)

while True:
    x = int(input(": "))
    if x == dado:
        print("Hai vinto")
        break
    else:
        print('Riprova')
    




