import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="mysql.playground.border0.io",
    port=3306,
    user="border0",
    password="Border0<3MySql",
    database="sys"
    )

df = pd.read_sql("SELECT * FROM sys_config;", conn)
print(df)
print(df.shape)

conn.close()