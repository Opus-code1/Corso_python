'''
Scrivi un programma che chieda tre 
numeri a, b, c all'utente e mostri il 
più grande tra loro.
'''
# === code === #
a, b, c = int(input("inserisci il primo numero: ")), int(input("inserisci il secondo numero: ")), int(input("inserisci il terzo numero: "))
if a == b and a == c and b == c:
    print("i numeri sono identici")
else:
    print(f"Il numero più grande tra {a,b,c} è il {max(a,b,c)}")
