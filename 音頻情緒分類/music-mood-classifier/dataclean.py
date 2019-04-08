import pandas as pd

df = pd.read_csv("SpotifyData/SpotifyList.csv")
print(df)
print(df.duplicated('song'))

df2 = df.drop_duplicats('song')
print(df2)
