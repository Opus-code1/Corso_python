import pandas as pd

for f, sep, atteso in [
    ('ordini.csv', ',', 300),
    ('clienti.csv', ';', 11),
    ('prodotti.csv', ',', 5),]:
    
    df = pd.read_csv(f, sep=sep)
    ok = "OK" if len(df) == atteso else 'NON OK'
    print(f"{ok} {f}: {df.shape} (atteso {atteso} righe)")