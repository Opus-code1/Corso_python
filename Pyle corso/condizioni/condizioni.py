# CONDIZIONI
nome = "admin"#input("Username: ")
password = "password123"#input("Password: ")

if nome == "admin": # 1
    if password == "password123": # 2
        print("Benvenuto") # 3
    
    else: 
        print("Password sbagliata")
else:
    print("Username sbagliato")
'''    
x = 5
if x > 4:
    if x == 4:
        if x != 5:
            if x < 3:
                if x >= 6:
                    pass
                if x <= 3:
                    pass
            if x == 2:
                pass
        if x is not 5:
            pass
'''
# if + else = else if -> elif 

x = 20
if x > 10:
    print(10)
if x < 30:
    print(30)
if x == 20:
    print(20)
elif x != 5:
    print(5)
else:
    print(2+2)




