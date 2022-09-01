import unicodedata
import re
import json
import os
from requests import get
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from bs4 import BeautifulSoup

import pandas as pd


def basic_clean(string):
    string = string.lower()
    string = unicodedata.normalize('NFKD', string)\
    .encode('ascii', 'ignore')\
    .decode('utf-8')
    string = re.sub(r"[^a-z0-9'\s]", '', string)
    return string



def tokenize(string):

    tokenizer = nltk.tokenize.ToktokTokenizer()

    return tokenizer.tokenize(string, return_str=True)


def stem(string):
    # Create the nltk stemmer object, then use it
    ps = nltk.porter.PorterStemmer()

    stems = [ps.stem(word) for word in string.split()]
    string_stemmed = ' '.join(stems)
    return string_stemmed


def lemmatize(string):
    #Create the nltk stemmer objest, then use it
    wnl = nltk.stem.WordNetLemmatizer()
    lemms = [wnl.lemmatize(word) for word in string.split()]
    string_lem = ''.join(lemms)

    return string_lem
    
def remove_stopwords(string, extra_words = [], exclude_words = []):
    '''
    This function takes in some text, optional extra_words and exclude_words parameters
    with default empty lists and returns the text after removing all stop words.
    '''
    # Create stopword_list
    stopword_list = stopwords.words('english')
    
    # Remove 'exclude_words' from stopword_list to keep these in my text.
    stopword_list = set(stopword_list) - set(exclude_words)
    
    # Add in 'extra_words' to stopword_list
    stopword_list = stopword_list.union(set(extra_words))
    
    # Split words in string.
    words = string.split()
    
    # Create a list of words from my string with stopwords removed and assign to variable.
    filtered_words = [word for word in words if word not in stopword_list]
    
    # Join words in the list back into strings and assign to a variable.
    string_without_stopwords = ' '.join(filtered_words)
    
    return string_without_stopwords