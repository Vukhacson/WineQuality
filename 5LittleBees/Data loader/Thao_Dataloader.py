import pandas as pd
path1 = 'Data set/winequality-red.csv'
path2 = 'Data set/winequality-white.csv'
red_wine = pd.read_csv(path1)
white_wine = pd.read_csv(path2)
print(red_wine.head())
print(white_wine.head())
