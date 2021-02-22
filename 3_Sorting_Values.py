import pandas as pd

df = pd.read_csv('pokemon_data.csv')

'''dane liczbowe'''
# print(df.describe())

''' sorting'''
# print(df.sort_values('Name'))
# print(df.sort_values('Name', ascending=False))

'''sort combinations'''

print(df.sort_values(['Type 1', 'Generation'], ascending=[1, 0]))
