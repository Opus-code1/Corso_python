'''
Scrivi una semplice funzione che, data una lista 
di numeri, fornisca in output un istogramma 
basato su questi numeri, usando asterischi per disegnarlo.

Data ad esempio la lista [3, 7, 9, 5], la funzione 
dovrà produrre questa sequenza:

***

*******

*********

*****
'''
# === CODICE === #
def ist(l):
    for i in l:
        print('*' * i)

ist([1,2,3,4,5,6,5,4,3,2,1])


