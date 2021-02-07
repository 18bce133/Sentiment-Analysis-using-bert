from nltk.stem.porter import PorterStemmer
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from transformers import BertTokenizer, TFBertForSequenceClassification
import tensorflow as tf
import os
import requests
import gdown

if not os.path.isfile('senti_weights.ckpt.data-00000-of-00001'):
    url = 'https://drive.google.com/u/1/uc?id=1me5NIopunCdZ8TEjVrUEB2ZbBDGjhVe7&export=download'
    output = 'senti_weights.ckpt.data-00000-of-00001'
    gdown.download(url, output, quiet=False)

def text_preprocess(sentence):
    sentence = sentence.replace("[^a-zA-Z#]", " ")
    with open('pickle_files/stopword.pickle','rb') as sp:
        stopwords = pickle.load(sp) 
    sentence = [item for item in sentence.lower().split(" ") if item not in stopwords and item != ""] #removing stopwords
    stemmer = PorterStemmer()
    sentence = [stemmer.stem(i) for i in sentence] #stemming the sentences
    sentence = " ".join(map(str,sentence))
    return sentence

def logistic_regression(sentence):
    sentence = text_preprocess(sentence)
    with open('pickle_files/lrmodel.pkl','rb') as mp:
        model = pickle.load(mp)
    result = model.predict_proba([sentence])[0][1]
    return int(result*100)
    
def text_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(text)
    if vs['pos'] > 0:
        return int(max(vs['neu'],vs['pos'])*100)
    return int((1-max(vs['neu'],vs['neg']))*100)
 
def bert_result(sentence):
    model = TFBertForSequenceClassification.from_pretrained("bert-base-uncased")
    tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
    model.load_weights("senti_weights.ckpt")
    tf_batch = tokenizer(sentence, max_length=128, padding=True, truncation=True, return_tensors='tf')
    tf_outputs = model(tf_batch)
    tf_predictions = tf.nn.softmax(tf_outputs[0], axis=-1)
    label = tf_predictions.numpy()
    return int(label[0][1]*100)

def retrieve_result(sentence):
    ans={}
    ans['Logistic regression']=logistic_regression(sentence)
    ans['Vader Analyzer']=text_sentiment_vader(sentence)
    ans['Bert Result']=bert_result(sentence)
    return ans