import pandas as pd

'''
Series non fa altro che associare un indice a un dato
'''
print("Series")
# Creare una Series da una lista
series = pd.Series(['10',15,20,25,30,35,40,45,50])
print(series)
print("________________________________")
# DATAFRAME
print('DataFrame\n')
dati = {
    'Nome':['Sarah', 'Pietro', 'Miriam'],
    'Età':[25, 20, 30],
    'Città':['Reggio', 'Roma', 'Torino'],
    'Animale': ['Cane', 'Panda', 'Gatto']
}
print(f'Prima:\n{dati}')
print("________________________________")
# Creare un DataFrame
'''
Qui creiamo un DataFrame 'df' utilizzando un dizionario 'dati'
'''
df = pd.DataFrame(dati)
print(f'Dopo:\n{df}')
print("________________________________")

print('Lettura File CVS')
# creo un DataFrame
file = "C:/Users/avare/Desktop/PyCorso/Lezione_11/username.csv"
df_1 = pd.read_csv(file)
print(df_1)
print("________________________________")

print("DataFrame Selezionato")
# Seleziona più colonne
df_s = df[['Età', 'Animale']]
print(df_s)
print("________________________________")

print('Aggiungere una nuova Colonna\n')
df['Stipendio'] = [40000, 50000, 45000]
print(df)

print("________________________________")
print("Calcolare la Media")
# età media
media_e = df['Età'].mean()
print(f'Età media {media_e}')
# stipendio medio
media_s = df['Stipendio'].mean()
print(f'Stipendio medio {media_s}')
print("________________________________")
print("Ordinare i Dati\n")
# DataFrame ordianto
# Età
df_ordinato = df.sort_values(by='Età')
print(df_ordinato)
print("________________________________")
# NOME
df_ordinato = df.sort_values(by='Nome')
print(df_ordinato)
print("________________________________")
print("Eliminare la Colonna")
df_eliminato = df.drop(columns=['Età'])
print(df_eliminato)









