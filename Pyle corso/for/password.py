nome_utente = "admin"
password = "admin"
log_in = False

for login in range(3):
    nu = input("Nome Utente: ")
    p = input("Password: ")
    if nu == nome_utente and p == password:
        print("log-in riuscito")
        log_in = True
        break
    else:
        print('Riprova')

if not log_in: # log_in == False:
    print("log-in non riuscito")
    
