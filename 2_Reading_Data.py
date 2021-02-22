import pandas as pd

df = pd.read_csv('pokemon_data.csv')

'''read headers'''
# print(df.columns)

''' read specific column'''
# print(df['Name'][0:5])
# print(df['Name', 'Type 1', 'HP'][0:5])

'''read specific row [Intiger LOCation]'''
# print(df.iloc[0:15:5])

'''read specific data [Location]'''
# print(df.loc[df['Type 1'] == "Grass"])
