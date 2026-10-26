import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="mysql.playground.border0.io",
    port=3306,
    user="border0",
    password="Border0<3MySql",
    database="sys"
    )

df = pd.read_sql("SELECT * FROM user_summary;", conn)
print("_" * 60)
print(df)
print("_" * 60)
print(df.head())
print("_" * 60)
print(df.columns.tolist())
print("_" * 60)
conn.close()