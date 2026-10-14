'''
PROVA PRATICA
_____________
creiamo un gioco molte vecchio quanto bello
Sasso Carta Forbici
immagino che lo conosciamo bene, se non è così
il giocatore sfida il computer
le regole sono semplici
- il giocatore sceglie tra [sasso carta forbici]
- il computer fa lo stesso

- il sasso batte le forbici
- le forbici battono la carta
- la carta batte il sasso
'''
# iniziamo importando la libreria random
import random

# adesso possiamo creare le varibili che tengono il conto dei punti
punti_giocatore = 0 # inizialmente 0
punti_computer = 0 # inizialmente 0

# ci serve il ciclo while per rendere tutto più bello
while True: # lo mettiamo a True per renderlo infinito
    
    # creiamo le condizioni di fine partita, che significa 
    if punti_giocatore >= 5 or punti_computer >= 5:
        
        # vediamo chi ha vinto, come si fa? Dobbiamo vedere
        if punti_computer > punti_giocatore:
            print("Ha vinto il computer")
        else:
            print("Ha vinto il giocatore")
    
    # andiamo al gioco adesso, ovvero il giocatore deve scegliere
    giocatore = input("Sasso-Carta-Forbici-> ")
    
    # bene adesso tocca al computer
    computer = random.randint(1, 3) # genera un numero casuale da 1 a 3
    
    # adesso mettiamo un paio di condizioni
    if computer == 1:
        computer = 'Sasso'
    elif computer == 2:
        computer = 'Carta'
    else:
        computer = 'Forbici'
    
    # stampiamo la sua scelta
    print(f"il computer sceglie {computer}")
    
    # molto bene ora dobbiamo vedere se sono pari
    if computer == giocatore:
        print("siete pari")
    
    # ottimo direi, ci manca far vicnere uno dei due, io scelgo il computer che vince
    if computer == 'Sasso' and giocatore == "Forbici": # sasso batte forbici
        print("Ha vinto il computer")
        
        # ha vinto, mettiamo i suoi punti
        punti_computer += 1
        
        # stampiamo i punti
        print(f"punti giocatore: {punti_giocatore}\npunti computer: {punti_computer}")
    
    
    elif computer == 'Carta' and giocatore == "Sasso": # carta batte sasso
        print("Ha vinto il computer")
        
        # ha vinto, mettiamo i suoi punti
        punti_computer += 1
        
        # stampiamo i punti
        print(f"punti giocatore: {punti_giocatore}\npunti computer: {punti_computer}")
        
    
    
    
    elif computer == 'Forbici' and giocatore == "Carta": # forbici battono carta
        print("Ha vinto il computer")
        
        # ha vinto, mettiamo i suoi punti
        punti_computer += 1
        
        # stampiamo i punti
        print(f"punti giocatore: {punti_giocatore}\npunti computer: {punti_computer}")
    
    #---------------------------------------------------------------------------------
    # dunque se non sono pari e il giocatore non perde, allora il giocatore vince, ci basta usare
    else:
        
        print("Ha vinto il giocatore")
        # ha vinto, mettiamo i suoi punti
        punti_giocatore += 1
        
        # stampiamo i punti
        print(f"punti giocatore: {punti_giocatore}\npunti computer: {punti_computer}")
        
# IL GIOCO FINISCE QUI
