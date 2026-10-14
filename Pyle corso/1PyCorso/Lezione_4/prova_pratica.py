for i in range(5):
    n = input("Nome utente: ")
    p = input("Password: ")
    #-----------------------
    if n == "roman" and p == "1234":
        print("benvenuto")
        break
    elif n != "roman" and p == "1234":
        print('nome utente sbagliato')
    elif n == "roman" and p != "1234":
        print("password sbagliata")
    else:
        print("nome utente e la password sono sbagliati")
    print("__________________________________________")

if p != '1234' or n != 'roman':
    print("hai finito i tentaivi")
