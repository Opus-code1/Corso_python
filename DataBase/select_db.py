import mysql.connector as msc
from mysql.connector import Error

conn = msc.connect(
    host="mysql.playground.border0.io",
    port=3306,
    user="border0",
    password="Border0<3MySql",
    database="sys"
    )

cursor = conn.cursor()
cursor.execute("SHOW TABLES;")
tabelle = cursor.fetchall()
print(f"Tabella nel databse: {tabelle}")

cursor.close()
conn.close()
'''
('books',)
('information_schema',)
('mysql',)
('performance_schema',)
('sys',)
'''
