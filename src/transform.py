import pandas as pd

def clean_column_names(df: pd.DataFrame):
    df=df.copy()
    df.columns=(
        df.columns.str.replace(" ","_")
    )
    return df


def fix_dates(df:pd.DataFrame):
    df=df.copy()
    df["Date"]=pd.to_datetime(df["Date"], errors="coerce")
    return df

def remove_duplicate_columns(df:pd.DataFrame):
    df=df.loc[:,~df.columns.duplicated()]
    return df

def melt_to_long_format(df:pd.DataFrame):
    value_cols=[c for c in df.columns if c != "Date"]
    df_long=df.melt(id_vars="Date", var_name="metric",value_name="value")
    return df_long

def transform(df:pd.DataFrame):
    print("Transforming Data")

    df=clean_column_names(df)
    df=fix_dates(df)
    df=remove_duplicate_columns(df)
    df=melt_to_long_format(df)

    print(f"Transformed into long format with {len(df)} rows")
    return df