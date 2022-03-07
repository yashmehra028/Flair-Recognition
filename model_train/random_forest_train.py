import pandas as pd
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import scipy.sparse as sp
import pickle


df = pd.read_csv("data/posts_by_flair.csv")
df['body'] = df['body'].fillna("")
print(df.info())
train_data = df[['title', 'body']]
flairs = df['flair']

vectorizer = CountVectorizer(min_df=0, lowercase=True, stop_words='english')
x_train_split, x_test_split, y_train, y_test = train_test_split(train_data, flairs, test_size=0.2, random_state=100)
vectorizer.fit(train_data['title'].values + (train_data['body'].values))

x_train = sp.hstack(x_train_split.apply(lambda col: vectorizer.transform(col)))
x_test = sp.hstack(x_test_split.apply(lambda col: vectorizer.transform(col)))

start = time.perf_counter()
classifier = RandomForestClassifier(n_estimators=10, n_jobs=-1)
classifier.fit(x_train, y_train)
score = classifier.score(x_test, y_test)
end = time.perf_counter()

print("Time taken :" + str(end - start))

print("Accuracy score :" + str(score))
