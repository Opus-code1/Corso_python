# FUNZIONI

# Livello 1: Definizione di una funzione senza argomenti
print("Livello 1")
def saluto():
    print("Ciao, Mondo!")

# per evocare la funzione
saluto()

# Livello 2: Definizione di una funzione con parametri/argomenti
print("\nLivello 2")
def saluto_nome(nome):
    print(f'Ciao {nome}')
# per evocare la funzione
# Metodo 1
saluto_nome("Carola")
# Metodo 2
nome = "Miriam"
saluto_nome(nome)

# Livello 3: Definizione di una funzione con un valore di ritorno
print("\nLivello 3")
def somma(x, y):
    risultato = x + y
    return risultato
# per evocare la funzione
risultato = somma(5, 9)
print(risultato)

# Livello 4: Definizione di una funzione con i valori stabiliti
print("\nLivello 4")
def nome(name = "Pietro"):
    print(f'Ciao {name}')
# per evocare la funzione
# Metodo 1
nome()
# Metodo 2
nome("Sarah")
# Metodo 3
name = "Jasmine"
nome(name)

# Livello 5: Definizione di una funzione con argomenti infiniti
print("\nLivello 5")
def somma_infinita(*args):
    risultato = sum(args)
    print(risultato)
    print(*args)
# per evocare la funzione
somma_infinita(1,2,3,4,5,6,7,8,9)

# Livello 6: Definizione di una funzione con valori stabiliti infiniti
print("\nLivello 6")
def valori_infiniti(**kwargs):
    if 'name' in kwargs:
        print(f'Ciao {kwargs['name']}')
    else:
        print("Ciao Mondo!")
    
# per evocare la funzione
valori_infiniti(name = "Katerina")


def stampa(*args, **kwargs):
    print(*args, **kwargs)

stampa(2+2)
stampa("ciao mondo")
x = 5
stampa(x)
for i in range(5):
    stampa(i)














