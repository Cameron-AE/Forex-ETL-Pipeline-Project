import pandas as pd
import sqlite3

conn=sqlite3.connect("db/forex.db")
df=pd.read_sql("SELECT*FROM forex_prices LIMIT 100", conn)

conn.close()

print(df)