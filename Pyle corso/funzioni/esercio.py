import random as r
import time as t
film = [
        "Inception", "Matrix", "Interstellar",
        "Fury Road", "Fight Club", "Whiplash "]
index = 1
# Funzione Visualizza
def visualizza():
    global index
    print('Film disponibili')
    for i in film:
        print(f'{index}-{i}')
        index += 1
        t.sleep(0.1)
    index = 1
    print("____________________________")
    t.sleep(0.5)
    menu()

# Funzione che aggiunge i film
def add():
    global film
    while True:
        agg = input("1-Aggiungi\n2-Esci\n-> ")
        while agg not in ["1", "2"]:
            print("Errore!")
            agg = input("1-Aggiungi\n2-Esci\n-> ")
        t.sleep(0.5)
        if agg == '1':
            nome = input("Nome Film: ")
            if nome in film:
                print("Il film è già nella lista")
            else:
                film.append(nome)
                t.sleep(0.5)
                print(f'{nome} è stato aggiunto nella lista!')
            
        elif agg == '2':
            t.sleep(0.5)
            menu()

# Funzione che elimina i film
def delete():
    while True:
        opzioni = input("1-Elimina\n2-Esci")
        while opzioni not in ["1", "2"]:
            print("Errore")
            opzioni = input("1-Elimina\n2-Esci\n-> ")
        if opzioni == "1":
            print("Film Disponibili")
            for i in film:
                print(i)
            nome = input("Nome film: ")
            if nome in film:
                t.sleep(0.5)
                film.remove(nome)
                print(f'{nome} Rimosso dalla lista!')
            else:
                t.sleep(0.5)
                print(f'Film non presente nella lista!')
        else:
            t.sleep(0.5)
            menu()

# Funzione che sceglie i film casuali
def random_film():
    num_film = int(input("Quanti film vuoi vedere?\n-> "))
    if num_film > len(film):
        print(f"Non hai abbastanza film da vedere nella lista\nHai soltanto {len(film)} film!")
        random_film()
    else:
        film_scelti = r.sample(film, num_film)
        print("Film casuali di oggi")
        for j in film_scelti:
            print(j)
            t.sleep(0.2)
        t.sleep(0.5)
        print("____________________________________")
        menu()

def close():
    print("___________________________")
    
def menu():
    print("Menu\n1-Visualizza i film\n2-Aggiungi film\n3-Elimina film\n4-Film casuale\n5-Esci\n")
    action = input("-> ")
    while action not in ['1','2','3','4','5']:
        print("Errore!")
        print("Menu\n1-Visualizza i film\n2-Aggiungi film\n3-Elimina film\n4-Film casuale\n5-Esci\n")
        action = input("-> ")
        
    if action == '1':
        visualizza()
        
    elif action == '2':
        add()
        
    elif action == '3':
        delete()
    
    elif action == "4":
        random_film()
    
    else:
        close()



