import pandas as pd
from tqdm import tqdm

data_path = '../data/result csv/'
df = pd.read_csv('../data/raw/all.csv')

for column in tqdm(df.columns):
    if column == 'ITM40':
        continue
    value_count = df[column].value_counts().sort_index()
    value_count.to_csv(data_path + f'{column.lower()}_value_counts.csv')