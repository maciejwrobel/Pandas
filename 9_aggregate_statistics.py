import pandas as pd

df = pd.read_csv('pokemon_data.csv')


'''średnia'''
# print(df.groupby(['Type 1']).mean())
# print(df.groupby(['Type 1']).mean().sort_values('Sp. Atk', ascending=False))

'''sum '''
# print(df.groupby(['Type 1']).sum())

'''count
żeby uporządkować, można dodac kolumnę 'counter' o wszystkich wartościach = 1, a następnie policzyć 'countera' '''
# print(df.groupby(['Type 1']).count())

df['counter'] = 1
# print(df.groupby(['Type 1']).count()['counter'])
'''subsets'''
print(df.groupby(['Type 1', 'Type 2']).count()['counter'])
