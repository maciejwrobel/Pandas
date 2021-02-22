import pandas as pd

df = pd.read_csv('pokemon_data.csv')

'''
# excel
df2 = pd.read_excel('pokemon_data.xlsx')

# notatnik (tab separated file)
df3 = pd.read_csv('pokemon_data.txt', delimiter='\t')
'''

print(df)

'''tylko kilka wierszy'''

print(df.head(3))
print(df.tail(3))
