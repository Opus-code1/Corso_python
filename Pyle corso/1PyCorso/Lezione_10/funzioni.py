'''
Le funzioni sono un modo molto comodo e professionale per gestire i codici
per creare una funzione si usa una parola chiave "def" e il nome della funzione
che segue le stesse regole delle variabili.

ci sono diverse tipi di funzione
'''

# Livello 1: Definizione di una funzione semplice, senza argomenti senza ritorno di dati
def saluto():
    print("Ciao, Mondo!")

# Evoccare questa fuznione
saluto() # Ciao, Mondo!

# Livello 2: Definizione di una funzione che prende i parametri
def saluto_nome(nome):
    print(f"Ciao, {nome}")

# Evocare questa funzione
# Metodo 1
saluto_nome("Zelda")
# Metodo 2
nome = "Zelda"
saluto_nome(nome)
# Medoto 3 (utilizzo input())
# //

# Livello 3: Definizione di una funzione con i Valori di Ritorno
def somma(a, b):
    return a + b

# Evocare questa funzione
risultato = somma(5, 3)
print(risultato) # 8

# Livello 4: Definizione di una funzioe con i valori stabiliti
def nome(n = "Zelda"):
    print(f"Ciao {n}")

# Evocare questa funzione
# Metodo 1
nome()
# Metodo 2
nome("Roman")

# Livello 5: Definizione che può prendere un numero infinito di varibili o dati
def somma(*args):
    return sum(args)

# Evocare questa fuznione
risultato = somma(1, 2, 3, 4)
print(risultato)

# Livello 6: Definizione che prende argomenti default infiniti
def saluto(**kwargs):
    if 'name' in kwargs:
        print(f'Hello {kwargs['name']}!')
    else:
        print("Ciao, Mondo!")

# Evocare questa funzione
# Metodo 1
saluto(name="Zelda")
# Metodo 2
saluto()

# Livello 6.5: Definziione di una fuznione senza limiti
def stampa(*args, **kwargs):
    print(*args, **kwargs)

# Evocare questa funzione
# Metodi sono moltissimi è come un print
# Esempio 1
nome = "Zelda"
#print(nome)
stampa(nome)
# Esempio 2
stampa("Ciao, Mondo!")
#print("Ciamo, Mondo!")
# Esempio 3
stampa(2 + 2)
# print(2 + 2)
# Esempio 4
stampa(f'Ciao {nome}')
# print(f'Ciao {nome}')
# Questa fuznione è il nostro nuovo print()

# Livello 7: Funzione che prende una fuznione come argomento
def applica(funzione, valore):
    return funzione(valore)

def quadrato(x):
    return x * x

# Evocare questa funzione
risultato = applica(quadrato, 5)
print(risultato)



