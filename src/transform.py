import pandas as pd

def clean_column_names(df: pd.DataFrame):
    df=df.copy()
    df.columns=(
        df.columns.str.replace(" ","_")
    )
    return df


def fix_dates(df:pd.DataFrame):
    df=df.copy()
    df["Date"]=df["Date"].astype(str).str.strip()
    df["Date"]=pd.to_datetime(df["Date"], errors="coerce")
    df=df.dropna(subset=["Date"]).reset_index(drop=True)
    return df

def remove_duplicate_columns(df:pd.DataFrame):
    df=df.loc[:,~df.columns.duplicated()]
    return df

def melt_to_long_format(df: pd.DataFrame):
    
    df = df.copy()
    
    
    value_cols = [c for c in df.columns if c != "Date"]
    df_long = df.melt(id_vars=['Date'], value_vars=value_cols,
                      var_name='metric', value_name='value')
    
    df_long = df_long.dropna(subset=['value']).reset_index(drop=True)
    
    return df_long

def split_metric(df: pd.DataFrame):
    df = df.copy()
    if "metric" in df.columns:
        df[['pair', 'type']] = df['metric'].str.split('_',n=1, expand=True)
    return df

def transform(df:pd.DataFrame):
    print("Transforming Data")

    df=clean_column_names(df)
    df=fix_dates(df)
    df=remove_duplicate_columns(df)
    df=melt_to_long_format(df)
    df=split_metric(df)

    print(f"Transformed into long format with {len(df)} rows")
    return df