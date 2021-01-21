import re
from nltk.util import pr
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
from nltk.stem.porter import *
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flair.models import TextClassifier
from flair.data import Sentence
import numpy as np

def text_preprocess(sentence):
    sentence = sentence.replace("[^a-zA-Z#]", " ")
    with open('pickle_files/stopword.pickle','rb') as sp:
        stopwords = pickle.load(sp) 
    sentence = [item for item in sentence.lower().split(" ") if item not in stopwords and item != ""] #removing stopwords
    stemmer = PorterStemmer()
    sentence = [stemmer.stem(i) for i in sentence] #stemming the sentences
    sentence = " ".join(map(str,sentence))
    return sentence

def predict_result(sentence):
    sentence = text_preprocess(sentence)
    with open('pickle_files/lrmodel.pkl','rb') as mp:
        model = pickle.load(mp)
    result = model.predict([sentence])[0]
    if result == 1:
        return "positive"
    return "negative"

print(predict_result(text_preprocess("My brother is sad")))

from textblob import TextBlob

def text_sentiment(text):
    testimonial = TextBlob(text)
    return int(testimonial.sentiment.polarity>0.5)
    

analyzer = SentimentIntensityAnalyzer()
def text_sentiment_vader(text):
 vs = analyzer.polarity_scores(text)
 return int(vs.get("compound")>0)
 
 
classifier = TextClassifier.load('en-sentiment')
def text_sentiment_flair(text):
  sentence = Sentence(text)
  classifier.predict(sentence)
  return np.round(sentence.labels[0].score)