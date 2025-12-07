# import pandas as pd


# df=pd.read_csv("raw/fx_data.csv")
# # Find rows where parsing fails
# for i, val in enumerate(df["date"]):
#     try:
#         pd.to_datetime(val)
#     except Exception as e:
#         print(i, val, e)