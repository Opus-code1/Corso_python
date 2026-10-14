import random as r

x = 0

def fine():
    print("Grazie per aver giocato!")
    exit()

def game():
    global x
    while True:
        y = int(input('Numero: '))
        if y == x:
            print('Hai vinto!')
            restart = input("Ricominciare? (si/no): ")
            if restart.lower() == 'si':
                randomize()
            else:
                fine()
        else:
            print("Riprova!")

def randomize():
    global x
    x = r.randint(1, 6)
    game()

randomize()
