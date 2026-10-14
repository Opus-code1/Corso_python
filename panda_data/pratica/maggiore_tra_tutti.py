'''
Scrivi un programma che, data 
una lista di numeri, fornisca in 
output il maggiore tra tutti 
gli elementi della lista.
'''
import random

numeri = []

num = int(input("quanti numeri: "))
for i in range(num):
    numeri.append(random.randint(1,100))
print(numeri)
print(f"Il numero più grande della lista è {max(numeri)}")