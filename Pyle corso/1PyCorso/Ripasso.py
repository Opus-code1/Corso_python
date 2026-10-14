#----------------------SPAZIO DEI DATI----------------------
# Variabili e costanti: assegnazione di valori
numero = 5  # variabile pubblica, accessibile ovunque
numeri = [1, 2, 3, 4, numero]

# Costanti, il cui valore non dovrebbe cambiare
PI = 3.14
VELOCITA_DELLA_LUCE = 299792458  # in m/s

# Variabili che rappresentano dati dell'utente
massa = 75  # kg
altezza = 1.70  # metri

#----------------------FUNZIONI----------------------
# Funzione che utilizza una variabile globale
def modifica_numero():
    '''
    Modifica il valore della variabile globale 'numero'.
    '''
    global numero  # Necessario per modificare una variabile globale all'interno di una funzione
    numero += 5  # Incrementa il valore globale di 'numero'
    return numero

#----------------------CLASSI----------------------
class Giocatore:
    '''
    Classe che rappresenta un giocatore.
    '''
    def __init__(self, nome, salute):
        self.nome = nome  # Variabile pubblica
        self.__salute = salute  # Variabile privata, non accessibile direttamente
    
    def mostra_salute(self):
        '''Ritorna il valore della salute (variabile privata).'''
        return self.__salute

# Esempio di istanza della classe Giocatore
giocatore1 = Giocatore("Eroe", 100)

#----------------------CONDIZIONI----------------------
# Condizioni if-elif-else
def scelta_condizioni(temperatura):
    '''
    Stabilisci un'azione in base alla temperatura.
    '''
    if temperatura == "caldo":
        return "Mi prendo un gelato."
    elif temperatura == "freddo":
        return "Mi prendo una pizza."
    else:
        return "Mi prendo un kebab."

#----------------------CICLI----------------------
# Ciclo while
def decisione_utente():
    '''
    Chiede all'utente una scelta finché non è valida.
    '''
    decisione = ""
    while decisione not in ["1", "2", "3"]:
        decisione = input("1-decisione 1\n2-decisione 2\n3-decisione 3\n")
    return decisione

# Ciclo for con range()
for i in range(5):  # Esegue un ciclo da 0 a 4
    pass  # placeholder

# Iterare attraverso una stringa
parola = "Esempio di frase"
for lettera in parola:
    pass  # placeholder per lavorare su ogni lettera

#----------------------ITERATORI----------------------
# Utilizzo degli iteratori in Python
lista = [1, 2, 3, 4, 5, 6]
iteratore = iter(lista)  # Crea un iteratore dalla lista

while True:
    try:
        elemento = next(iteratore)  # Ottiene il prossimo elemento
        print(elemento)
    except StopIteration:  # Si ferma quando non ci sono più elementi
        break

#----------------------TIPI DI DATI----------------------
# Tipi di dati comuni in Python
numero = 10  # int
decimale = 10.5  # float
testo = "ciao"  # str
booleano = True  # bool
lista = [1, 2, 3]  # list
dizionario = {"chiave": "valore"}  # dict
tupla = (1, 2, 3)  # tuple
insieme = {1, 2, 3}  # set
# bytearray, None, range(), ecc.

#----------------------CLASSI E EREDITARIETÀ----------------------
class Persona:
    '''
    Classe madre Persona.
    '''
    def __init__(self, nome):
        self.nome = nome  # Variabile pubblica

class Studente(Persona):
    '''
    Classe figlia Studente, eredita da Persona.
    '''
    def __init__(self, nome, corso):
        super().__init__(nome)  # Inizializza il costruttore della classe madre
        self.corso = corso

class Professore(Persona):
    '''
    Classe figlia Professore, eredita da Persona.
    '''
    def __init__(self, nome, materia):
        super().__init__(nome)
        self.materia = materia  # Variabile pubblica aggiunta

# Esempi di utilizzo delle classi
studente1 = Studente("Mario", "Matematica")
professore1 = Professore("Giovanni", "Fisica")

#----------------------IMPORT E MODULI----------------------
import time  # Modulo importato -> import nome modulo
import time as t # Modulo importato -> import nome modulo come nome
from time import sleep # Dal Modulo nome importa funzione
from time import sleep as s# Dal Modulo nome importa funzione come nome


#----------------------FUNZIONI----------------------
# Funzione che utilizza una variabile globale
def modifica_numero():
    '''
    Modifica il valore della variabile globale 'numero'.
    '''
    global numero  # Necessario per modificare una variabile globale all'interno di una funzione
    numero += 5  # Incrementa il valore globale di 'numero'
    return numero

#----------------------RETURN----------------------
def somma(a, b):
    '''
    Restituisce la somma di due numeri.
    '''
    return a + b  # Restituisce il risultato della somma

# Chiamata della funzione somma
risultato = somma(3, 5)
print(f"La somma di 3 e 5 è: {risultato}")  # Stampa 8

# Funzione senza return esplicito
def saluta():
    '''
    Stampa un messaggio di saluto. Non restituisce alcun valore.
    '''
    print("Ciao!")

saluta()  # Esegue la funzione ma non restituisce nulla

#----------------------ENUMERATE----------------------
# Enumerate restituisce l'indice e l'elemento in un ciclo
parole = ["cane", "gatto", "uccello"]

for indice, animale in enumerate(parole):
    print(f"{indice}: {animale}")
    # Stampa: 
    # 0: cane
    # 1: gatto
    # 2: uccello

#----------------------MANIPOLAZIONE DI FILE----------------------

# Apertura e manipolazione dei file in Python
# Ci sono vari modi per aprire e lavorare con i file:
# 'r' -> lettura (read), 'w' -> scrittura (write), 'a' -> append, 'b' -> modalità binaria

# Modo 1: Apertura di un file per lettura
def leggi_file(nome_file):
    '''Legge e stampa il contenuto di un file'''
    try:
        with open(nome_file, 'r') as file:  # 'r' indica che vogliamo solo leggere
            contenuto = file.read()  # Legge tutto il file
            print(contenuto)  # Stampa il contenuto del file
    except FileNotFoundError:
        print("Il file non esiste.")

# Modo 2: Scrittura in un file (sovrascrive il contenuto esistente)
def scrivi_file(nome_file, contenuto):
    '''Scrive nel file, sovrascrivendo il contenuto esistente.'''
    with open(nome_file, 'w') as file:  # 'w' indica scrittura
        file.write(contenuto)  # Scrive il contenuto nel file

# Modo 3: Aggiungere contenuto a un file esistente
def aggiungi_al_file(nome_file, nuovo_contenuto):
    '''Aggiunge nuovo contenuto alla fine di un file esistente.'''
    with open(nome_file, 'a') as file:  # 'a' indica aggiunta
        file.write(nuovo_contenuto)

# Modo 4: Lettura riga per riga
def leggi_file_righe(nome_file):
    '''Legge il file riga per riga.'''
    try:
        with open(nome_file, 'r') as file:
            for riga in file:
                print(riga.strip())  # Stampa ogni riga senza spazi inutili
    except FileNotFoundError:
        print("Il file non esiste.")

# Esempi di utilizzo:
# scrivi_file('esempio.txt', 'Questo è un nuovo file.\n')
# aggiungi_al_file('esempio.txt', 'Aggiungiamo un po\' di testo.\n')
# leggi_file('esempio.txt')
# leggi_file_righe('esempio.txt')

#----------------------MODI DI MANIPOLARE FILE----------------------

# 1. 'r' (read): apre il file in modalità lettura. Se il file non esiste, solleva un errore.
# 2. 'w' (write): apre il file in modalità scrittura, sovrascrivendo il file. Se il file non esiste, lo crea.
# 3. 'a' (append): apre il file in modalità aggiunta. Se il file non esiste, lo crea.
# 4. 'b' (binary): modalità binaria, utile per file non di testo (immagini, video, ecc.).

# Modo 5: Lettura di un file binario
def leggi_file_binario(nome_file):
    '''Legge un file in modalità binaria.'''
    with open(nome_file, 'rb') as file:  # 'rb' indica lettura binaria
        contenuto = file.read()
        print(contenuto)

# Modo 6: Scrittura in un file binario
def scrivi_file_binario(nome_file, dati):
    '''Scrive dati in modalità binaria.'''
    with open(nome_file, 'wb') as file:  # 'wb' indica scrittura binaria
        file.write(dati)

#----------------------CHIAMATA DELLE FUNZIONI----------------------
# Testare funzioni di lettura e scrittura file
# scrivi_file('testo.txt', 'Ciao, questo è un testo di esempio.\n')
# leggi_file('testo.txt')
# aggiungi_al_file('testo.txt', 'Aggiungo un’altra linea di testo.\n')
# leggi_file_righe('testo.txt')

# Creare e manipolare file binari (ad esempio, per immagini o dati binari)
# scrivi_file_binario('esempio.bin', b'Dati binari di esempio.')
# leggi_file_binario('esempio.bin')

#----------------------TIPO BONUS----------------------
# 'with' è utilizzato per gestire i file in modo sicuro: apre il file e lo chiude automaticamente dopo l'uso

