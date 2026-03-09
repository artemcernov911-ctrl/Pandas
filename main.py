import pandas as pd

df = pd.read_csv('Indian Liver Patient Dataset (ILPD).csv')
print(df.head())
print(df.info())
print(df.describe())