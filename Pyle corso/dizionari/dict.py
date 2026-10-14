# DIZIONARI
'''
-Mutabili -> sono molto manipolabili
-Iniche Chiavi -> ogni chiave è unica
-Non ordinati -> non hanno un ordine preciso
1-Dove? 
2-Quale? (tipo di dato)
3-Come? 
'''
#         key   value |  key value | key     value
dati = {"Nome":"Zelda", "Età":28, "Città": "Catania"}

# chiave:valore
#----------------------------------------------------
oggetti = {
    'palla':"è un oggetto rotondo che rimbalza",
    'matita':"è un oggetto che ci permette di scrivere",
    'macchina':"è un veicolo che ci permette di spostarci",
    'USB':"è un oggetto che può contenere i dati"
    }

print("\n_________________________________________________________\n")
print('prima:',oggetti)

palla = oggetti["palla"]
matita = oggetti["matita"]
macchina = oggetti["macchina"]
usb = oggetti["USB"]

print("\n_________________________________________________________\n")
print(f'la palla {palla}')
print(f'la matita {matita}')
print(f'la macchina {macchina}')
print(f'la USB {usb}')

print("\n_________________________________________________________\n")
# MODIFICARE UN DATO
print('Dato Modificato')
oggetti["matita"] = "è un oggetto che ci permette di scrivere e disegnare"
print(f'la matita {oggetti["matita"]}')

print("\n_________________________________________________________\n")
# ELIMINARE UN DATO
print('Dato Eliminato')
del oggetti["macchina"]
print('dopo:',oggetti)

print("\n_________________________________________________________\n")
# AGGIUNGERE UN DATO
print("Dato Aggiunto")
# diz -  chiave   :  valore
oggetti["cuffie"] = "un oggetto che ci permette di ascoltare la musica"
print(oggetti["cuffie"])
print("\n_________________________________________________________\n")
# STAMPARE SOLO LE CHIAVI
chiavi = oggetti.keys()
print(chiavi)

print("\n_________________________________________________________\n")

# STAMPARE SOLO I VALORI
valori = oggetti.values()
print(valori)

print("\n_________________________________________________________\n")

# SVOTARE IL DIZIONARIO
oggetti.clear()
print(oggetti)

print("_________________________________________________________\n")

num_stud = int(input("Numero Studenti: "))
studenti = {}
for i in range(num_stud):
    nome = input("Nome: ")
    anni = int(input("Età: "))
    corso = input("Corso di Studio: ")
    studenti["Nome Studente "+str(i+1)+":"] = nome
    studenti["Età Studente "+str(i+1)+":"] = anni
    studenti["Corso Studente "+str(i+1)+":"] = corso
    print("____________________________________\n")

print("______________________________")
for chiave, valore in studenti.items():
    print(f"{chiave}\n{valore}")


inventario = {"spada di diamante": 1, "mele": 20, "carbone": 64, "pietra": 36}

player_stats = {
                "HP": 100,
                "MP": 60,
                "Attack": 25, 
                "M-DF": 150, 
                "F-DF": 350, 
                "A-Speed": 10,
                "Dodge": 20,
                "Accur": 42
                }
