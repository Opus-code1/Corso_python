#            1           2        3         4          5
frigo = ["biscotti", "latte", "cereali", "panino", "kinder"]

print(frigo)
for i in range(3):
    remove = int(input("Indice: "))

    frigo.pop(remove)

    print(frigo)





