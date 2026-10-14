# lista = ['ciao','panda','rosso','mela','celeste','macchina',1,2,3,4,5,6,7]

# # CERCA IN LISTA #
# dato = "ciao"
# if dato in lista:
#     print(f"si {dato} è nella lista")
# else:
#     print(f"no {dato} non è nella lista")

menu = [
    'lasagna','carbonara',
    'tortellini','margherita',
    'kebab','cotoletta'
]

if input("nome piatto: ") in menu:
    print("Si c'è")
else:
    print("No, non è nel menu")
