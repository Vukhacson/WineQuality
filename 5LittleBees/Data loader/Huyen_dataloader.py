import pandas as pd
path1='D:\GITHUB\Data set\winequality-red.csv'
path2='D:\GITHUB\Data set\winequality-white.csv'
wine_red=pd.read_csv(path1)
wine_white=pd.read_csv(path2)
print(wine_red.head())
print(wine_white.head())