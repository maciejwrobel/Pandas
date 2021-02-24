import pandas as pd

df = pd.read_csv('pokemon_data.csv')

# print(df.loc[df['Type 1'] == 'Grass'])

'''multiple conditions in (df['Column_name'] == 'Condition')   and -> &, or -> |'''
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# print(new_df)



''' reseting index as new df'''

new_df = new_df.reset_index()
print(new_df)
new_df.to_csv('filtered.csv')

''' reseting index inplace (need memory)'''
new_df.reset_index(drop=True, inplace=True)

