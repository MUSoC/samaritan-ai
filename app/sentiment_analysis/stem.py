import pandas as pd
import numpy as np
import re, nltk        
from nltk.stem.porter import PorterStemmer

def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed