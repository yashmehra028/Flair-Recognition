import praw
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


reddit = praw.Reddit(client_id='biHuZNftcyXJNw',
                     client_secret='NBRuoUNvSSuRp60IqlKZon7l474',
                     user_agent='Learning Curve',
                     username='UltimateFox69',
                     password='ABCD1234')

subreddit = reddit.subreddit('india')

flair_df = pd.read_csv('data/flair_map.csv')
flair_df.set_index('Flair_name', inplace=True)

#subreddit.search('flair:"Foreign Relations"')

topics_dict = {"title": [],
               "body": [],
               "score": [],
               "flair": [],
               "flair_id": [],
               }


for flair in flair_df.index:
    sub = subreddit.search(f'flair:"{flair}"')
    for submission in sub:
        try:
            topics_dict["title"].append(submission.title)
            topics_dict['body'].append(submission.selftext)
            topics_dict["score"].append(submission.score)
            topics_dict["flair"].append(flair)
            topics_dict['flair_id'].append(flair_df.loc[flair])

        except:
            pass


# for i in topics_dict:
#     print(i, len(topics_dict[i]))
topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('data/posts_by_flair.csv')
