import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="mysql.playground.border0.io",
    port=3306,
    user="border0",
    password="Border0<3MySql",
    database="sys"
    )

df = pd.read_sql("""
                SELECT query, exec_count, total_latency, avg_latency
                FROM statement_analysis
                ORDER BY exec_count  DESC
                LIMIT 5;
                """, conn)

print(df)