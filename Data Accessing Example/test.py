import pandas as pd

path = "Data set/winequality-white.csv"

df = pd.read_csv(path, delimiter=";")
print(df.head())
print(df.shape)