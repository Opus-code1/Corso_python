# === LIVELLO 1 === #
'Funzione semplice: senza argomenti'
def nome():
    pass # codice dentro

# Evocare la funzione
nome()

# Esempio
def saluto():
    print('Ciao')

saluto()

# === LIVELLO 2 === #
'funzione semplice con argomenti'
def nome(arg1, arg2, arg3):
    pass # codice

# Evocare Metodo 1
nome('valore 1', 'valore 2', 'valore 3')
# Evocare Metodo 2
nome(arg1='valore1', arg2='Valore2', arg3='Valore3') 
# Evocare Metodo 3
nome(arg2='valore2', arg1='Valore1', arg3='Valore3')
# Evocare Metodo 4
nome(arg2='valore2', arg3='Valore3', arg1='Valore1')

# Esempio
def salutoNome(nome):
    print(f"Ciao {nome}")

salutoNome("Celeste") # Ciao Celeste

def presenta(nome, cognome, anni,  studio):
    print(f"Ciao mi chiamo {nome} {cognome} ho {anni} anni e studio {studio}")

presenta('Celeste', 'Rossi', 23, 'Matematica')
# === LIVELLO 3 === #
'funzione con argomenti con valori stabiliti'
def nome(arg1="ciao", arg2=15, arg3=False):
    pass # codice

# Evocare Metodo 1
nome()
# Evocare Metodo 2
nome('marco', [1,2,3], True)
# Evocare Metodo 3
nome(arg2 = 28)
# Evocare Metodo 4
nome(arg1='panda', arg3=True)

# Esempio:
def presenta(nome="Celeste", cognome="Rossi", anni=23,  studio="Matematica"):
    print(f"Ciao mi chiamo {nome} {cognome} ho {anni} anni e studio {studio}")

# ====================================== #
presenta()
presenta(nome="Andrea")
presenta(cognome="Verdi", studio="Biologia")

# === LIVELLO 4 === #
'funzione con type data args'
# Evocare Metodo 1
def nome(arg1:int, arg2:str, arg3: bool):
    pass # codice funzione

def presenta(nome:str="Celeste", cognome:str="Rossi", anni:int=23,  studio:str="Matematica"):
    print(f"Ciao mi chiamo {nome} {cognome} ho {anni} anni e studio {studio}")

