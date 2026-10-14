menu = ['pizza', 'pesce', 'carne', 'sushi', 'pasta']

domanda = input(": ")


if domanda in menu:
    print(f"Si {domanda} è nel menù")
else:
    print(f"No {domanda} non è nel menù")
    