def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b != 0:
        return a / b
    else:
        return "Impossibile dividere per zero"

while True:
    print("Seleziona un'operazione:")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Esci")

    scelta = input("Inserisci il numero corrispondente all'operazione desiderata: ")

    if scelta == '5':
        print("Arrivederci!")
        break

    if scelta not in ('1', '2', '3', '4'):
        print("Scelta non valida. Riprova.")
        continue

    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    if scelta == '1':
        print("Risultato:", somma(num1, num2))
    elif scelta == '2':
        print("Risultato:", sottrazione(num1, num2))
    elif scelta == '3':
        print("Risultato:", moltiplicazione(num1, num2))
    elif scelta == '4':
        print("Risultato:", divisione(num1, num2))
