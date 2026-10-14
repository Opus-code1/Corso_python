scelta = input("=== SCEGLI ===\n+\n-\n/\nx\n\n: ")

if scelta == "+":
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    
    print(f"{num1} + {num2} = {num1 + num2}")

elif scelta == "-":
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    
    somma = num1 - num2
    
    print(f"{num1} - {num2} = {somma}")

elif scelta == "/":
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    
    risultato = f"{num1} / {num2} = {num1 / num2}"
    print(risultato)

elif scelta == "x" or scelta == "X" or scelta == "*":
    num1 = float(input("Numero 1: "))
    num2 = float(input("Numero 2: "))
    somma = num1 * num2
    risultato = f"{num1} x {num2} = {somma}"
    print(risultato)

else:
    print('Scelta non valida!')
