import re
from nltk.util import pr
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import string
from nltk.stem.porter import *
import pickle

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