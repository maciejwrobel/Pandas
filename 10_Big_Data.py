import pandas as pd

df = pd.read_csv('pokemon_data.csv')

new_df = pd.DataFrame(columns=df.columns)

for df in pd.read_csv('pokemon_data.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, results])
    print('chunked df')
    print(new_df)
