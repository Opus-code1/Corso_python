# Variabile è un contenitore di dati
variabile_1 = 5
ciao = 1
Ciao = 2
CIAO = 3
var_1 = 5
_ = 7
# a = 5
# b = 6
# c = 8
# d = 10
a, b, c, d, e, f, g = 1, "Sarah", 3.14, False, 5, 15, 8
print(c)

print(ciao)
print(Ciao)
print(CIAO)
print(ciao + Ciao + CIAO)

'''
if elif else for and or not in is while print
'''
Print = 5
print(Print)

# TIPI DI VARIABILI

'''
INTERO = int() = 1 | 5 | 10 | 25
REALE = float() = 3.14 | 5.05 | 1.0
STRINGA = str() = "parola" | '5'
BOOLEANO = bool() = True | False
'''
print("_____________________________________________")
x = 5 # int()
y = 3.14 # float()
z = "7" # str()
print(x)
print(y)
print(z * 2)
print("_____________________________________________")

# CONVERSIONE DI TIPI
'''
int -> float
int -> str
float -> int
float -> str
str -> int
str -> float
str(5) # "parola"
'''
a = 5
b = 5.5
c = '7'
print(f'a: {a} {type(a)}\nb: {b} {type(b)}\nc: {c} {type(c)}')
print("_____________________________________________")

x = float(a)
y = int(b)
z = int(c)

print(f'a: {x} {type(x)}\nb: {y} {type(y)}\nc: {z} {type(z)}')

print("_____________________________________________")

nome = input("come ti chiami?\n->")
print(f'Ciao {nome}')

print(type(nome))

print("_____________________________________________")

a = float(input("primo numero: "))
b = float(input("secondo numero: "))
print(f'{a} + {b} = {a + b}')
print(f'{a} + {b} = {int(a + b)}')
print("_____________________________________________")

log = input("Log-In: ")
password = input("Password: ")
print('Benvenuto!')



