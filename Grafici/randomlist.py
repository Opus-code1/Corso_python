import random

def list_num(lung=5, minimo=1, massimo=10, tipo="int"):
    lista = []
    for _ in range(lung):
        if tipo == 'int': num = random.randint(minimo, massimo)
        else: num = random.uniform(minimo, massimo)
        
        lista.append(num)
    return lista

