import os
import pandas as pd
perc = './panda_data/vendite.csv'

# Leggiamo il nostro file
df = pd.read_csv(perc)

if not os.path.exists("./panda_data/vendite.xlsx"):
    df.to_excel("./panda_data/vendite.xlsx", index=False)

if not os.path.exists("./panda_data/vendite.html"):
    df.to_html("./panda_data/vendite.html", index=False)
