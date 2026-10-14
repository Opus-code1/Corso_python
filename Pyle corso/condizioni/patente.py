anni = int(input("anni: "))

# bugfix
if anni <= 0:
    print("mi sembra impossibile")
if anni >= 100:
    print("penso tu sia ansiano per guidare")
elif anni < 18:
    print("non puoi prendere la patente")
    print(f"ti mancano ancora {18 - anni} anni")
elif anni >= 18:
    print("puoi prendere la patente")