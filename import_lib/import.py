'''
=== IMPORTARE ===
import nome_modulo
import random

=== USARE ===
nome_modulo.funzione(argomento1=valore, argomento_n=valore,...)
random.randint(a=1, b=5)
----------------------------------------------------------------
=== IMPORTARE CON IL NOME ===
import nome_modulo as nm
import random as r

=== USARE ===
nm.funzione(arg1=value, arg_n=value,...)
r.randint(b=10, a=5)
----------------------------------------------------------------

=== MULTI-LINE IMPORT ===
import modulo1
import modulo2
import modulo_n

import random
import time
import pandas

=== USARE ===
random.randint(a=1, b=5)
time.sleep(0.5)
----------------------------------------------------------------
=== ONE-LINE MULTI IMPORT V1 ===
import modulo_1, modulo_2, modulo_n, ...
import random, time, tkinter, ...

=== USARE ===
random.randint(a=1, b=5)
time.sleep(0.5)
...

----------------------------------------------------------------
=== ONE-LINE MULTI IMPORT V2 ===
import (modulo_1, modulo_2,
        modulo_3, modulo_n)
import (random, time,
        os, sys, pandas)

=== USARE ===
random.randint(a=1, b=5)
time.sleep(0.5)
os.getcwd()
----------------------------------------------------------------
=== FROM IMPORT ===
from modulo import funzione
from random import randint


=== USARE ===
funzione(argomenti e valori)
randint(1, 6)


----------------------------------------------------------------
=== FROM IMPORT CON IL NOME ===
from modulo import funzione as fnz
from random import randint as r

=== USARE ===
fnz(...)
r(1, 10)
----------------------------------------------------------------
=== FROM IMPORT MULTI-FUNZIONI ===
from modulo import funione_1. fuznione_2, ...
from random import randint, choice, choices

=== USARE ===
funzione_1()
randint(1, 5)
choice([1,2,3])
'''
