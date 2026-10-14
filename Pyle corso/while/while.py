# il ciclo WHILE
import random
# affinchè io sono VERO eseguo il codice

num = int(input("numero: "))
t = 0
while True:
    x = random.randint(1,100)
    print(x)
    t += 1
    if x == num:
        print(f'{num} indovinato in {t} tentativi')
        break
    
    
    
