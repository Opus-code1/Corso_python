'''
Scrivi una funzione che, data una stringa 
come parametro, restituisca un dizionario 
rappresentante la "frequenza di comparsa" 
di ciascun carattere componente la stringa.

Per fare un esempio, data una stringa 
"ababcc", otterremo in risultato 
{"a": 2, "b": 2, "c": 2}
'''

def car(x:str=""):
    d = {}
    for l in x:
        if l in d: d[l] += 1
        else: d[l] = 1
    return d

print(car("abcdeefgbadac"))
