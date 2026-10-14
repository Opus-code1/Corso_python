import pandas as pd
import numpy as np

# Creo un DataFrame di valori casuali
np.random.seed(42)
data = np.random.rand(100, 3)# 100 righe e tre colonne
# DataFrame
df = pd.DataFrame(data, columns=["X", "Y", "Z"])

# Calcolo la correlazione tra le colonne del DataFrame
cor = df.corr()
print(cor)


