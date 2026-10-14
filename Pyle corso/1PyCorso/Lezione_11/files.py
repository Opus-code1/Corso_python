# READ MODE
with open("file.txt", 'r') as file:
    print(file.read())

# WRITE MODE  
with open("file.txt", 'w') as file:
    file.write("testo da mettere nel file")

# APPEND MODE  
with open("file.txt", 'a') as file:
    file.write("testo da mettere nel file")

# CREATE MODE  
with open("file.txt", 'x') as file:
    pass
