import pandas as pd
from config import RAW_DATA_PATH

def extract() -> pd.DataFrame:
    print("Extracting raw data...")
    df=pd.read_csv(RAW_DATA_PATH)
    print(f"Extracted {len(df)} rows")
    return df

