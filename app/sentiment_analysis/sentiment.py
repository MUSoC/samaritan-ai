import pandas as pd
import numpy as np
import re, nltk
from sklearn.feature_extraction.text import CountVectorizer        
from nltk.stem.porter import PorterStemmer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import random

test_file = 'test_data.csv'
train_file = 'train_data.csv'

test_df = pd.read_csv(test_file, header=None, delimiter="\t", quoting=3)
test_df.columns = ["Text"]
train_df = pd.read_csv(train_file, header=None, delimiter="\t", quoting=3)
train_df.columns = ["Sentiment","Text"]

print train_df.shape
print test_df.shape

print train_df.head()
print test_df.head()

print train_df.Sentiment.value_counts()

print np.mean([len(s.split(" ")) for s in train_df.Text])

stemmer = PorterStemmer()
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem_tokens(tokens, stemmer)
    return stems

vectorizer = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokenize,
    lowercase = True,
    stop_words = 'english',
    max_features = 85
)

corpus_data_features = vectorizer.fit_transform(train_df.Text.tolist() + test_df.Text.tolist())

corpus_data_features_nd = corpus_data_features.toarray()
print corpus_data_features_nd.shape

vocab = vectorizer.get_feature_names()
print vocab

dist = np.sum(corpus_data_features_nd, axis=0)
for tag, count in zip(vocab, dist):
    print count, tag

X_train, X_test, y_train, y_test  = train_test_split(
    corpus_data_features_nd[0:len(train_df)], 
    train_df.Sentiment,
    train_size=0.85, 
    random_state=1234)

log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)

y_pred = log_model.predict(X_test)

print(classification_report(y_test, y_pred))

log_model = LogisticRegression()
log_model = log_model.fit(X=corpus_data_features_nd[0:len(train_df)], y=train_df.Sentiment)

test_pred = log_model.predict(corpus_data_features_nd[len(train_df):])

spl = random.sample(xrange(len(test_pred)), 25)
"""
# last object sentiment
spl = len(test_pred) - 1
print test_pred[spl]

"""
for text, sentiment in zip(test_df.Text[spl], test_pred[spl]):
    print sentiment, text