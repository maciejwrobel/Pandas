import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')


'''regex conditions. opposite ~ '''
# print(df.loc[df['Name'].str.contains('Mega')])
# print(df.loc[~df['Name'].str.contains('Mega')])

# print(df.loc[df['Type 1'].str.contains('Fire|Grass', regex=True)])

'''re.I -> ignore case'''
# print(df.loc[df['Type 1'].str.contains('fire|grass', flags=re.I, regex=True)])


print(df.loc[df['Name'].str.contains('^pi[a-z]*', flags=re.I, regex=True)])
