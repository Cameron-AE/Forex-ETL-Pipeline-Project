import pandas as pd
import sqlite3

conn = sqlite3.connect("db/forex.db")
df = pd.read_sql("SELECT * FROM forex_prices where Date is null", conn)
conn.close()

# # Convert Date to datetime explicitly
# df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

# # Show rows where Date became NaT
# missing_dates = df[df['Date'].isna()]
# print(missing_dates)
# print("Number of truly missing/invalid dates:", len(missing_dates))


print(df)