import random
nome = "Zelda"
anni = 28
altezza = 1.62582
print("Mi chiamo", nome, "e ho", anni, "anni")
print(f"Mi chiamo {nome} e ho {anni} anni")
print('Mi chiamo {} e ho {} anni e mi piace {}, domani mi sveglio alle 0{}:00'.format(nome, anni, "ballare", 8))
print("oggi è una {0} giornata, fuori {1}".format("bella", "c'è il sole", "nuvolosa"))

print("Domani {m} esco con {p} alle {o}".format(m = "Sera", p = "Sarah", o = 21))
print("Mi chiamo {} e ho {:02} anni".format(nome, anni))
print(f"Mi chiamo {nome} e sono alta {altezza:.2f} metri")
#-----------------------------------------------------------
# ALLINEAMENTO DEL TESTO
'''
< SINISTRA
> DESTRA
^ CENTRO
'''
# : muro < a sinistra di pixel -> :<10
print("Nome: {:<10}Età: {:>5}".format(nome, anni))

print("{}".format(nome))
print("{:*^20}".format(nome))

casuale = random.random()
print(f'{casuale:.2f}')

