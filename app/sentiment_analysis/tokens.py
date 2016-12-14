import pandas as pd
import numpy as np
import re, nltk
import stem

stemmer = stem.PorterStemmer()

def tokenize(text):
    text = re.sub("[^a-zA-Z]", " ", text)
    tokens = nltk.word_tokenize(text)
    stems = stem.stem_tokens(tokens, stemmer)
    return stems