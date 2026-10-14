# Crea un file
# with open("nome_file.txt", "x") as f:
#     print("file creato")

def crea_file(nome:str="file.txt", debug=True):
    with open(nome, "x") as f:
        if debug:
            print("il file è stato creato")

if __name__ == "__main__":
    crea_file()
    crea_file("esempio.py")
    crea_file("esempio.txt", debug=False)
    crea_file(debug=False, nome="esempio.json")
