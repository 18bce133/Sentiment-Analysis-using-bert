from nltk.stem.porter import PorterStemmer
import pickle
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flair.models import TextClassifier
from flair.data import Sentence

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
 
def text_sentiment_flair(text):
    classifier = TextClassifier.load('en-sentiment')
    sentence = Sentence(text)
    classifier.predict(sentence)
    return int(sentence.labels[0].score*100)

def retrieve_result(sentence):
    ans={}
    ans['Logistic regression']=logistic_regression(sentence)
    ans['Vader Analyzer']=text_sentiment_vader(sentence)
    ans['Flar Analyzer']=text_sentiment_flair(sentence)
    return ans