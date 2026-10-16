import random

def list_num(lung=5, minimo=1, massimo=10):
    lista = []
    for _ in range(lung):
        num = random.randint(minimo, massimo)
        lista.append(num)
    return lista
