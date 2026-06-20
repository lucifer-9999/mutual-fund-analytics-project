import pandas as pd

df = pd.read_csv("data/raw/scheme_performance.csv")

print(df.columns.tolist())

print(df.head())