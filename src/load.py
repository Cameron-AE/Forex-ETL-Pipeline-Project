import sqlite3
from config import DB_PATH,TABLE_NAME

def load(df):
    print(f"Loading data into SQlite Database at {DB_PATH}")

    conn=sqlite3.connect(DB_PATH)
    df.to_sql(TABLE_NAME,conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()


    print("Load complete.")


