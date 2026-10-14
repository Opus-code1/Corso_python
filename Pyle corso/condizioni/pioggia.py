# pioggia
print("tu: Posso uscire?")
prima_domanda = input("mamma: Fuori piove?\n->")

if prima_domanda == "si":
    seconda_domanda = input("mamma: Hai l'ombrello?\n-> ")
    if seconda_domanda == "si":
        print("mamma: esci pure")
    elif seconda_domanda == "no":
        print("mamma: aspetta che smetta di piovere")
    else:
        print("mamma: non ho capito")
elif prima_domanda == "no":
    print("mamma: esci pure")
else:
    print("mamma: non ho capito")




