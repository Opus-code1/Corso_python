#i = 0 -> 1 -> 2 -> 3 -4
for i in range(5):
    print(i) # iteratore
    # 0
    # 1
    # 2
    # 3
    # 4
print('__________________________________')
# Minimo e Massimo
for i in range(10, 101):
    print(i)
print('__________________________________')
# Passo Positivo
for i in range(0, 11, 2):
    print(i)

print('__________________________________')
# Passo Negativo
for i in range(10, 0, -1):
    print(i)

print('__________________________________')
# index 012345
nome = "Carola"
# |c = 0|a = 1|r = 2|o = 3|l = 4|a = 5|
print (f'{nome[0]}{nome[1]}{nome[2]}{nome[3]}{nome[4]}{nome[5]}\n\n')

for lettere in nome:
    print(lettere)


