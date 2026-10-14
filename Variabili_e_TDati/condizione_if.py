semaforo = input("colore: ")

if semaforo == "rosso": # CONDIZONE MADRE
    print("Sto fermo") # FIGLIO

if semaforo == "giallo":
    print("Passa ma sta attento")

if semaforo == "verde":
    print("Passa pure")

# else:
#     print("colore non esiste")

'''
x = 5 → tu x sei 5!
x == 5 → tu x sei 5?
↓
True
False


Cartella_docs
    ╚Rac_Foto
        ╚foto_cane.png
'''
nome_cartella = "Cartella_docs"
nome_s_cartella = "Rac_Foto"

if nome_cartella == "Cartella_docs": # True
    if nome_s_cartella == "Rac_Foto": # True
        print("foto_cane.png")


"""
---- OPERATORI DI CONFRONTO ----

== → uguale a → un dato è IDENTICO  a... | 5 == 5 → True "5" == 5 → False
> → maggiore di | un numero è più grande di un altro | 5 > 3 → True 7 > 9 → False
< → minore di | un numero è più piccolo di un altro
>= → maggiore di OPPURE uguale a
<= → minore di OPPURE uguale a
"""

anni = 15
if anni >= 18:
    print("puoi prendere la patente")

# else:
#     print("non puoi prendere la patente!")

