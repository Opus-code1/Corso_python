# === REGOLE PER LE VARIABILI === #
'''
• Le avriabili NON possono contenere gli pazi nei nomi
SBAGLIATO ↓
nome persona = "Celeste"
    Perchè?
    • nome → è una variabile 
    • nome persone → "persona" diventa una seconda variabile

GIUSTO ↓
nomepersona = "Sarah"
nome_persona = "Celeste"
nomePersona = "Alessia"
NomePeRsoNa="Marco"

• Una variabile NON può iniziare con un numero
SBAGLIATO ↓
1nome = "Mario"

GIUSTO ↓
nome1 = "ciao"
n0m3 = "Luca"

• Una variabile NON può avere nessun simbolo  ma solo "_"
SBAGLIATO ↓
nome-person@ = "Celeste"

GIUSTO ↓
nome_persona = "Clara"
_ = "ciao"
__ = 15
___ = _ 
____ = __ + 15

• Una variabile NON può contenere i nomi RISERVATI
if, elif, else, print, in, is, while, True, False, None, for, range, or, not, and

SBAGLIATO ↓
print = 15

GIUSTO ↓
Print = 15
print(Print)
'''
