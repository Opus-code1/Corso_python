import mysql.connector as msc
from mysql.connector import Error

conn = msc.connect(
    host="mysql.playground.border0.io",
    port=3306,
    user="border0",
    password="Border0<3MySql",
    database="sys"
    )
if conn.is_connected():
    print('ok')

cursor = conn.cursor()
cursor.execute("SELECT * FROM sys_config LIMIT 3;")

righe = cursor.fetchall()
for riga in righe:
    print(riga)

cursor.close()
conn.close()