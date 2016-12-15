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

test_file = 'test_data.csv'
train_file = 'train_data.csv'

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

vocab = vectorizer.get_feature_names()

dist = np.sum(corpus_data_features_nd, axis=0)

X_train, X_test, y_train, y_test  = train_test_split(
    corpus_data_features_nd[0:len(train_df)], 
    train_df.Sentiment,
    train_size=0.85, 
    random_state=1234)

log_model = LogisticRegression()
log_model = log_model.fit(X=X_train, y=y_train)

y_pred = log_model.predict(X_test)

print (classification_report(y_test, y_pred))

log_model = LogisticRegression()
log_model = log_model.fit(X=corpus_data_features_nd[0:len(train_df)], y=train_df.Sentiment)

# Save model using joblib
joblib.dump(log_model, 'sentiment.pkl')