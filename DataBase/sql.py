# https://freesql.com/
# === CONNECTOR === #
# pip install mysql-connector-python

'''
mysql-connector-python
↓ 
è come un traduttore tra python e MySQL
creato da Oracle → i creatori di MySQL
'''
import mysql.connector as msc
from mysql.connector import Error

try:
    conn = msc.connect(
        host="mysql.playground.border0.io",
        port=3306,
        user="border0",
        password="Border0<3MySql",
        )
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES;")
    
    for db in cursor.fetchall():
        print(db)
    # chiudi cursore e conn
    cursor.close()
    conn.close()
    
except Error as e: print(f"Errore: {e}")
