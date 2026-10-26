import pandas as pd
import numpy as np
from pathlib import Path

def s(l=60): print('_' * l)

def titolo(t): print(f"=== {t} ===")

def check():
    # VERIFICA LA PRESENZA FILE #
    titolo("VERIFICA FILE DI INPUT")

    FILES = {
        'ordini.csv': (',', 300),
        'clienti.csv': (';', 11),
        'prodotti.csv': (',', 5),
    }

    for nome, (sep, atteso) in FILES.items():
        if not Path(nome).exists():
            raise FileNotFoundError("File mancante")
        _df = pd.read_csv(nome, sep=sep)
        ok = "OK" if len(_df) == atteso else "NON OK"
        print(f"{ok} {nome}: shape={_df.shape} - (atteso {atteso} righe)")
check()

ordini = pd.read_csv('ordini.csv')
clienti = pd.read_csv('clienti.csv', sep=";")
prodotti = pd.read_csv('prodotti.csv')


titolo("PULIZIA ORDINI")
# Scartiamo ordini non riconoscibili
n_prima = len(ordini)
ordini_clean = ordini.dropna(subset=['id_cliente', 'id_prodotto']).copy()
n_dopo = len(ordini_clean)

s()
print(f"Numero Prima: {n_prima}\nNumero Dopo: {n_dopo}")
s()
print(ordini_clean)
s()

ordini_clean['id_cliente'] = ordini_clean['id_cliente'].astype(int)
ordini_clean['id_prodotto'] = ordini_clean['id_prodotto'].astype(int)

print(ordini_clean)
s()

n_qta_nan = int(ordini_clean['quantita'].isna().sum())
mediana_qta = ordini_clean['quantita'].median()
ordini_clean['quantita'] = (ordini_clean['quantita'].fillna(mediana_qta).astype(int))
print(ordini_clean)
s()

titolo("PULIZIA DATE")
def parse_data_mista(valore):
    if pd.isna(valore):
        return pd.NaT
    # Formati presenti nel dataset
    for fmt in ('%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y', '%d-%m-%Y'):
        try:
            return pd.to_datetime(valore, format=fmt)
        except (ValueError, TypeError):
            continue
    return pd.NaT

ordini_clean['data'] = ordini_clean['data'].apply(parse_data_mista)
n_date_rotte = int(ordini_clean['data'].isna().sum())
print(f"Date non ordinate: {n_date_rotte}")
s()
assert n_date_rotte == 0, f"ci sono {n_date_rotte} date rotte"

def pulisci_importo(x):
    if pd.isna(x):
        return np.nan
    s_ = str(x).replace("€", '').replace(' ', '').strip()
    if s_ == '':
        return np.nan
    try:
        return float(s_)
    except ValueError:
        return np.nan
    
mask_vuoti_prima = ordini_clean['importo'].isna() | (ordini_clean['importo'] == '')

n_importi_vuoti = int(mask_vuoti_prima.sum())

ordini_clean['importo'] = ordini_clean['importo'].apply(pulisci_importo)

n_importi_nan = int(ordini_clean['importo'].isna().sum())

print(f"importi vuoti: {n_importi_vuoti} | dopo la pulizia: {n_importi_nan}")

assert n_importi_nan == n_importi_vuoti, f"Attesi: {n_importi_vuoti} NaN, trovati {n_importi_nan}"

ordini_clean['anno'] = ordini_clean['data'].dt.year
ordini_clean['mese'] = ordini_clean['data'].dt.month

MESI_IT = {1:'Gen',2:'Feb',3:'Mar',4:'Apr',5:'Mag',6:'Giu',7:'Lug',8:'Ago',9:'Set',10:'Ott',11:'Nov',12:'Dic'}

ordini_clean['mese_nome'] = ordini_clean['mese'].map(MESI_IT)

titolo('PULIZIA PRODOTTI')
prodotti_clean = prodotti.copy()
assert prodotti_clean['id_prodotto'].is_unique, 'id prodotti duplicati'
assert prodotti_clean['prezzo_listino'].notna().all(), 'prezzi mancanti'
assert (prodotti_clean['prezzo_listino'] > 0).all, 'prezzi non validi'
print(f"Prodotti: {len(prodotti_clean)}")


titolo("CHECK FINALE")
print(f"Righe: {len(ordini_clean)}")
print(f"dtype data: {ordini_clean['data']}")
print(f"dtype importo: {ordini_clean['importo']}")
print(f"dtype quantita: {ordini_clean['quantita']}")
print(f"importi NaN: {ordini_clean['importo'].isna().sum()}")
s()
assert ordini_clean['data'].notna().all(), "date mancanti"
assert ordini_clean['quantita'].notna().all(), 'quantita mancanti'
assert ordini_clean['importo'].dtype == 'float64', 'importo non è float'
assert ordini_clean['data'].dtype.kind == 'M', 'data non è data type'

titolo("PULIZIA CLIENTI")

print(clienti['citta'].value_counts(dropna=False).head(10))

clienti['citta'] = (clienti['citta'].str.strip().str.title().replace('', np.nan))

print(clienti['citta'].value_counts(dropna=False).head(10))


n_clienti_prima = len(clienti)
clienti_clean = clienti.drop_duplicates(subset='id_cliente', keep='first').copy()

s()

n_clienti_dopo = len(clienti_clean)
print(f"Clineti prima: {n_clienti_prima}\nClienti Dopo:{n_clienti_dopo}")
s()

clienti_clean['ha_email'] = clienti_clean['email'].notna()

assert len(clienti_clean) == 10, 'attesi 10 clienti'
assert clienti_clean['id_cliente'].is_unique, 'clienti duplicati'


# MERGE
titolo('MERGE')

df = (
    ordini_clean.merge(clienti_clean, on='id_cliente', how='left').merge(prodotti_clean, on='id_prodotto', how='left')
)

s()
print(df)
s()

assert df['nome'].notna().all(), 'ordini senza clienti'
assert df['nome_prodotto'].notna().all(), 'ordini senza prodotto'

mask_importo_nan = df['importo'].isna()
n_ricostruiti = int(mask_importo_nan.sum())

df.loc[mask_importo_nan, 'importo'] = (
    df.loc[mask_importo_nan, 'prezzo_listino'] * df.loc[mask_importo_nan, 'quantita']
)

assert df['importo'].isna().sum() == 0, 'importi mancanti'

print(f'importi ricostruiti: {n_ricostruiti}')

# === SALVATAGGIO === #
titolo("SALVATAGGIO")

# df.to_parquet('ordini_puliti.parquet', index=False)
df.to_csv('ordini_puliti.csv', index=False)
print("Fatto")
