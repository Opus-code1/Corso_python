'''
FUNZIONI

print() stampa
str() converte
len() lunghezza
typ() tipo di dato

MODULI
import turtle, random

CLASSI
variabile = turtle.Turtle() # classe

METODI
variabile.color("blue") # metodo

random.randint() # metodo
'''
# MODULO STRING
import string
# METODI DEL MODULO
string.ascii_letters # contiene tutte le lettere maiuscole e minuscole
print(string.ascii_letters)
string.ascii_lowercase # contiene tutte le lettere minuscole
print(string.ascii_lowercase)
string.ascii_uppercase # contiene tutte le lettere maiuscole
print(string.ascii_uppercase)
string.digits # contiene tutti i numeri
print(string.digits)
string.punctuation # coniene tutti i caratteri di punteggiatura
print(string.punctuation)
string.whitespace # contiene tutti i caratteri come spazio bianco
print(string.whitespace)
print('_____________________________________________________')
nome = "sarah sta Dormendo Adesso"
print(f'normale: {nome}')
print('_____________________________________________________')
maiuscola = nome.capitalize() # strasforma la prima lettera in maiuscolo
print(f'capitalize: {maiuscola}')
print('_____________________________________________________')
t_min = nome.lower()
print(f'lower: {t_min}')
print('_____________________________________________________')
t_mai = nome.upper()
print(f'upper: {t_mai}')
print('_____________________________________________________')
num = nome.isdigit()
print(num)
up = nome.isupper()
print(up)
print('_____________________________________________________')

nome = "si"#input(": ").lower()
if nome == "si":
    print("panda")
    
elif nome == "no":
    print("koala")
    
else:
    print("verde")
print('_____________________________________________________')

#---------------------------------------------
# JOIN
parole = ['ciao', 'come', 'stai', '?']
print(parole)
unione = " ".join(parole)
print(unione)
stringa = "è una giornata nuvolosa"
unione = "*".join(stringa)
print(unione)



