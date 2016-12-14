import pandas as pd
import numpy as np
import re, nltk
from sklearn.feature_extraction.text import CountVectorizer        
from nltk.stem.porter import PorterStemmer
from sklearn.cross_validation import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import random
from sklearn.externals import joblib
import tokens

train_file = 'train_data.csv'
test_file = 'test_data.csv'
test_df = pd.read_csv(test_file, header=None, delimiter="\t", quoting=3)
test_df.columns = ["Text"]
train_df = pd.read_csv(train_file, header=None, delimiter="\t", quoting=3)
train_df.columns = ["Sentiment","Text"]

vectorizer = CountVectorizer(
    analyzer = 'word',
    tokenizer = tokens.tokenize,
    lowercase = True,
    stop_words = 'english',
    max_features = 85
)

corpus_data_features = vectorizer.fit_transform(train_df.Text.tolist() + test_df.Text.tolist())
corpus_data_features_nd = corpus_data_features.toarray()

# Load model again
classifier = joblib.load('sentiment.pkl')

test_pred = classifier.predict(corpus_data_features_nd[len(test_df):])

spl = random.sample(xrange(len(test_pred)), 25)
"""
# last object sentiment
spl = len(test_pred) - 1
print test_pred[spl]

"""
for text, sentiment in zip(test_df.Text[spl], test_pred[spl]):
    print sentiment, text