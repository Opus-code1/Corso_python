import mysql.connector as msc
from connect_db import connect
import pandas as pd

conn = connect()
cursore = conn.cursor()

def create_db(nome_db="test"):
    cursore.execute(f"CREATE DATABASE IF NOT EXISTS {nome_db};")

    # create_db("scuola")
    cursore.close()
    conn.close()

# === SELECT NEW DATABASE === #
# conn = connect(db="scuola")

# ========================================== #
# === CREARE UNA TABELLA === #
def crea_tabella():
    cursore.execute("""
                    CREATE TABLE IF NOT EXISTS studenti (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        nome VARCHAR(50) NOT NULL,
                        anni INT,
                        voto DECIMAL(4,1)
                    );
                    """)
    cursore.close()
    conn.close()
# crea_tabella()

def crea_tab_time():
    cursore.execute('''
                    CREATE TABLE IF NOT EXISTS log_accessi (
                        id INT PRIMARY KEY AUTO_INCREMENT,
                        evento VARCHAR(100),
                        creato_il TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                    ''')
    cursore.close()
    conn.close()
# crea_tab_time()

# === INSERIMENTO DATI === #
def inserisci_dati(nome, anni, voto, tabella):
    cursore.execute(f'INSERT INTO {tabella} (nome, anni, voto) VALUES (%s, %s, %s);', (nome, anni, voto))
    
    conn.commit()
    
    print(f"Inserita {nome}: {cursore.lastrowid}")

# inserisci_dati('Sarah', 21, 18.0, 'studenti')
# inserisci_dati('Pietro', 21, 19.2, 'studenti')
# inserisci_dati('Luca', 23, 26.5, 'studenti')
# inserisci_dati('Andrea', 22, 29.0, 'studenti')
# inserisci_dati('Alessia', 24, 27.5, 'studenti')

# ====================================================== #

def inserisci_multi(list, tabella):
    dati = list
    cursore.executemany(f'INSERT INTO {tabella} (nome, anni, voto) VALUES (%s, %s, %s);', dati)
    conn.commit()
    print(f"inserite {cursore.rowcount} righe")

studenti = [
    ('Alessando', 25, 26.0),
    ('Aurora', 26, 19.5),
    ('Mario', 20, 28.0),
    ('Luigi', 22, 30.0)
    ]
# inserisci_multi(studenti, 'studenti')

# === LEGGERE I DATI === #
def lettura_dati(obj, tabella, t=1):
    cursore.execute(f"SELECT {obj} FROM {tabella};")
    if t == 1:
        for riga in cursore.fetchall():
            print(riga)
    else:
        print('_' * 60)
        for i,n,a,v in cursore.fetchall():
            print(f"ID: {i} - Nome: {n} - Anni:{a} - Voto: {v}")
    cursore.close()
    conn.close()

# lettura_dati('*', 'studenti')
# print("_" * 60)
# lettura_dati('*', 'studenti', t=2)

def lettura_filtro():
    cursore.execute("SELECT nome, voto FROM studenti WHERE anni > %s;", (24,))
    dati = cursore.fetchall()
    print(dati)
    print("_" * 60)
    for d in dati:
        print(d)
    cursore.close()
    conn.close()

# lettura_filtro()

def filter_ordine():
    cursore.execute("SELECT * FROM studenti ORDER BY voto DESC LIMIT 2;")
    dati = cursore.fetchall()
    print(dati)
    cursore.close()
    conn.close()

# filter_ordine()

def filter_agg():
    cursore.execute("SELECT COUNT(*), AVG(voto), MAX(voto) FROM studenti;")
    dati = cursore.fetchall()
    print(dati)
    cursore.close()
    conn.close()
    
# filter_agg()


# === LEGGERE DATABASE DA PANDAS === #

# df = pd.read_sql("SELECT * FROM studenti;", conn)
# print(df)

# === AGGIORNARE I DATI === #
def update_data(tab:str, obj:str, cond:str, value: tuple):
    cursore.execute(f'UPDATE {tab} SET {obj} = %s WHERE {cond} = %s;', value)
    conn.commit()
    print("Fatto")
    cursore.close()
    conn.close()

# update_data('studenti', 'voto', 'nome', (30.0, "Aurora"))

# === ELIMINARE I DATI === #
def elimina_dati(tab:str, cond:str, value:tuple):
    cursore.execute(f"DELETE FROM {tab} WHERE {cond} = %s;", value)
    conn.commit()
    print('fatto')
    cursore.close()
    conn.close()
    
# elimina_dati('studenti', 'id', (9,))

# === DELETE TUTTI I RECORD === #

def elimina_record():
    cursore.execute("DELETE FROM studenti;")
    conn.commit()

# elimina_record()

# === DELETE TABLE === #

def elimina_tab():
    cursore.execute("DROP TABLE IF EXISTS studenti")

# elimina_tab()

# === ELIMINARE INTERO DATABASE === #
def elimina_database(nome_database):
    conferma = input("ELIMINARE IL DATABASE?\ns/n → ").lower()
    if conferma in ['s','si','y','ye','yes']:
        cursore.execute(f"DROP DATABASE IF EXISTS {nome_database}")
    else:
        print("...")

elimina_database('test')