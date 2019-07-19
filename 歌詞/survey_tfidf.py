import csv
import pandas as pd
df = pd.read_csv('lyrics_data/survey_tfidf.csv')
lyrics0 = df['lyrics'][0]
print(lyrics0)
