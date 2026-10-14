
'''
Un array è una struttura di dati che contiene una
collezione ordinata di elementi, tutti dello stesso tipo
ogni elemento di un array è identificato con un indice che 
va da 0 in su.
'''
# nome_array = [1,2,3] # è una lista per python
# print(type(nome_array))

# NUMPY
import numpy as np

# CREARE UN ARRAY
arr = np.array([1,2,3,4]) # tutti interi
print(arr)
print("_________________________________________")
# CREARE UN ARRAY MULTIDIMENSIONALE
arr = np.array([[1, 2], [3, 4], [5, 6]])
print(arr)

print("_________________________________________")
# CREARE UN ARRAY DI ZERI
#                col-rig
zeros = np.zeros((3, 3))
print(zeros)
print("_________________________________________")

# CREARE UN ARRAY DI ONES
#             col-rig
one = np.ones((3, 3))
print(one)
print("_________________________________________")
# ARRAY DI NUMERI CONSECUTIVI
consec = np.arange(10) # simile alla funzione range del for
print(consec)
print("_________________________________________")
# ARRAY DI NUMERI CON INTERVALLO
interval = np.arange(0, 10, 2)
print(interval)
print("_________________________________________")
# SOMMA DI ARRAY
arr_1 = np.array([1, 2, 3])
arr_2 = np.array([4, 5, 6])
somma = arr_1 - arr_2
print(somma)
print("_________________________________________")
# PRODOTTO MATRICE
mat_1 = np.array([[1, 2], [3, 4]])
mat_2 = np.array([[5, 6], [7, 8]])
mat_prod = np.dot(mat_1, mat_1)
print(mat_prod)
print("_________________________________________")
# GENRARE NUMERI CASUALI
rand_arr = np.random.rand(5)
print(rand_arr)
print("_________________________________________")

print("_________________________________________")
# GENERARE UNA MATRICE CASUALE
rand_mat = np.random.rand(3, 3)
print(rand_mat)
print("_________________________________________")
# CALCOLARE LA MEDIA DI UN ARRAY
arr = np.array([1,2,3,4,5,6,7,8,9])
mean_val = np.mean(arr)
print(mean_val)
print("_________________________________________")
# CALCOLARE UNA DEVIAZIONE STANDARD
arr = np.array([1,2,3,4,5,6,7,8,9])
std_val = np.std(arr)
print(std_val)
print("_________________________________________")
# SOMMA LUNGO UN ASSE
mat = np.array([[1, 2], [3, 4], [5, 6]])
somma = np.sum(mat, axis=1)
print(somma)
print("_________________________________________")
# TRASPOSTA DI UNAMATRICE
mat = np.array([[1, 2], [3, 4], [5, 6]])
tras = np.transpose(mat)
print(tras)
print("_________________________________________")
# VALORI MASSIMI E MINIMI
arr = np.array([1,2,3,4,5,6,7,8,9])
max_val = np.max(arr)
min_val = np.min(arr)
print(f'Valore Massimo di un array: {max_val}\nValore Minimo di un array: {min_val}')
print("_________________________________________")
# VERIFICARE CONDIZIONI SU UN ARRAY
arr = np.array([1,2,3,4,5,6,7,8,9])
cond = arr > 5
print(cond)
nome = "Sarah"
print("_________________________________________")
# INDICI DEGLI ELEMENTI
arr = np.array([1,2,3,4,5,6,7,8,9])
indici = np.where(arr)
print(indici)
print("_________________________________________")
