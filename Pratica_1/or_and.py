'''
# OR 
nome = "Celeste"

if nome == "Celeste" or nome == "Marco" or nome == "Alessia":
    print('puoi entrare')
else:
    print("non sei nella lista")

classe = ("Celeste", "Marco", "Givanni")

print(classe)

if "Celeste" in classe:
    print("Presente")

if "p" in "ciao, oggi ho visto un panda allo zoo":
    print("la lettera p esiste nella frase")


with open("nomi.txt", "r") as x:
    nomi = x.read()
    print(nomi)
    if "marco" in nomi:
        print("Marco è presente")
'''

# AND 
classe = ["marco", "alessia", "celeste", "luca"]

if "marco" in classe and "alessia" in classe and "celeste" in classe and "luca" in classe:
    print("iniziamo la lezione")
else:
    print("manca qualcuno, aspettaimo!")
