import pandas as pd

df = pd.read_csv('data/hot_posts.csv')

df = df[['flair', 'flair_id']]

flair_map = {}

for flair in df['flair'].unique():
    filt = df['flair'] == flair
    filt_df = df[filt]

    flair_id = filt_df['flair_id'].unique()[0]

    flair_map[flair] = flair_id

df1 = pd.Series(flair_map)
df1 = df1.to_frame()
df1.rename(columns={0: 'Flair_id'}, inplace=True)
df1.to_csv('data/flair_map.csv')
