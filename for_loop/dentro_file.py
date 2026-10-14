stringa_file = ""

with open("file.txt", "r") as f:
    stringa_file = f.read()

lista = []

for lettera in stringa_file:
    if lettera == "c":
        break
    lista.append(lettera)
    print(lettera)

print(f"Sono statae stampate: {len(lista)} lettere (spazi inclusi)")

