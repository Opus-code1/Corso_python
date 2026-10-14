import pandas as pd

perc = './panda_data/vendite.csv'
# apro il file con with
with open(perc, 'r') as file:
    contenuto = file.read()

df = pd.read_csv(perc)
print(df)

print("▄" * 80)
df = pd.read_csv(perc, header=None)
print(df)

print("▄" * 80)
df = pd.read_csv(perc, header=None, names=['•', '█', '▄', '▀', 'ª', '☺', '☻', '♣'])
print(df)

