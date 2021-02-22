import pandas as pd

df = pd.read_csv('pokemon_data.csv')


'''saving /without index'''
# df.to_csv('modified.csv', index=False)

'''to Excel -> pip install openpyxl'''
# df.to_excel('modified.xlsx', index=False)

''' tab separator, notatnik'''
df.to_csv('modified.txt', index=False, sep='\t')