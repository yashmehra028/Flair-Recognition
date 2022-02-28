import praw
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib
# matplotlib.rcParams['font.family'] = 'serif'
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='biHuZNftcyXJNw',
                     client_secret='NBRuoUNvSSuRp60IqlKZon7l474',
                     user_agent='Learning Curve',
                     username='UltimateFox69',
                     password='ABCD1234')

subreddit = reddit.subreddit('india')

topics_dict = { "title":[],
                "body":[],
                "score":[],
                "flair":[],
                "flair_id":[], 
                "num_comments":[]}


for submission in subreddit.hot(limit=1000):
    topics_dict["title"].append(submission.title)
    topics_dict['body'].append(submission.selftext)
    topics_dict["score"].append(submission.score)
    topics_dict["flair"].append(submission.link_flair_text)
    topics_dict['flair_id'].append(submission.link_flair_template_id)
    topics_dict["num_comments"].append(submission.num_comments)

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv("data/hot_posts.csv")