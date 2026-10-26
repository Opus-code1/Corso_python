import mysql.connector as msc

conn = msc.connect(
    host="mysql.playground.border0.io",
    port=3306,
    user="border0",
    password="Border0<3MySql",
    database="sys"
    )

cursor = conn.cursor()
query = "SELECT * FROM sys_config WHERE variable LIKE %s LIMIT 3;"

cursor.execute(query, ('%max%',))
for riga in cursor.fetchall():
    print(riga)