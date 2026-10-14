import pandas as pd
import numpy as np

# Creiamo un array di numeri casuali (5 righe e 3 colonne)
np_array = np.random.rand(5, 3)
# Creiamo un DataFrame Pandas
df = pd.DataFrame(np_array, columns=["A", "B", "C"])

# Stampa il tutto
print(df)