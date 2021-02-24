import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')

'''CONDITION : wszystkie, które w kolumnie [type 1] mają 'fire'
SET PARAMETER : zamień wartośc kolumny na 'Flamer '''

# df.loc[df['Type 1'] == "Fire", 'Type 1'] = 'Flamer'
# df.loc[df['Type 1'] == "Fire", 'Legendary'] = True


'''many parameters'''
df.loc[df['HP'] > 50, ['Generation', 'Legendary']] = ['best one', 'Leeeeegendary']
print(df)


