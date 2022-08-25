import pandas as pd
path1 = 'Data set/winequality-red.csv'
path2 = 'Data set/winequality-white.csv'
red_df = pd.read_csv(path1)
white_df = pd.read_csv(path2)
print(red_df.head())
print(white_df.head())