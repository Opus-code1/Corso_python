# ================================================ #
# RANGE SEMPLICE 
'range(max)'
for i in range(5):
    pass
    # si esegue per un masismo di 5 volte
    # 0
    # 1
    #...
    #4
    

# RANGE MIN-MAX
'range(min, max)'
for i in range(5, 10):
    pass # pass = non fare nulla
    # 0 X
    # 1 X
    # 2 X
    #...
    # 5
    # 6
    #...
    # 9

# RANGE SALTERINO
'range(min, max, step)'
for i in range(1, 11, 2):
    break
    print(i)
    # 0 
    # 1 X
    # 2 
    # 3 X
    # 4 

from time import sleep as s
# RANGE NEGATIVO
'range(max, min, -step)'
for i in range(10, 0, -2):
    break
    s(1)
    print(i)

