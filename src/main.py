from extract import extract
from transform import transform
from load import load


def main():
    df_raw=extract()
    df_clean=transform(df_raw)
    load(df_clean)

if __name__=="__main__":
    main()