import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# print(df.head(5))

'''adding new column, double check !!!'''
df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# print(df.sort_values('Total', ascending=False))

'''dropping column'''
df = df.drop(columns=['Total'])

'''alternative adding column method'''
df['Total'] = df.iloc[:, 4:10].sum(axis=1)

# print(df.head(5))

'''rearenging columns, !!! single column in [] because it will be read as string !!!'''
cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head(5))

