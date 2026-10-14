# === TIPI DI DATI === #
'''
STRINGHE 
str → str() | stringa

NUMERI
int → int() | intero
float → float() | reale (con la virgola)
comlex → complex() | complesso

BOOLEANI
bool → bool() | booleano → True o False


# ================================================== #
str → int
str → float
str → bool

int → str
int → float
int → bool

float → int
float → str
float → bool
'''

# PRAICA #
anni = 25

tipo = type(anni)
print(tipo)

# == conv == #
'in   cosa'
anni = float(anni)

print(float(anni)) # print(anni)
print(type(anni))

anni = str(anni)

print(str(anni))
print(type(anni))

anni = bool(anni)
print(bool(anni))
print(type(anni))

str(15)
int("142")
float(12)
int(3.14)
