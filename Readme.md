<h2>This project is the implementation of BERT model on Twitter Sentiment Dataset.</h2>

Dataset link :- <a>https://www.kaggle.com/kazanova/sentiment140</a> contains 1.6 million tweets with their sentiments.

Training was done in colab environment with 25gb RAM and GPU, it tooks nealry 9 hours for training for single epoch only and results are impressive with 85% accuracy.

Trained model was also converted to REST API with flask and embedded in webapp.

Libraries used :- 
<ul>
  <li> nltk</li>
<li>pandas</li>
<li>pickle-mixin</li>
<li>scikit-learn</li>
<li>flask</li>
<li>tweepy</li>
<li>python-dotenv</li>
<li>vaderSentiment</li>
<li>tensorflow-cpu</li>
<li>transformers==3.5.1</li></li>
<li>gdrive</li></li>
<li>gdown</li>
<li>gunicorn</li>
  </ul>

To use on local machine :- 
<ul>
  <li>git clone https://github.com/18bce133/Sentiment-Analysis-using-bert.git</li>
  <li>pip install -r requirements.txt</li>
  <li>python app.py</li>
  <li>In browser type http://127.0.0.1:5000/</li>
  </ul>

Note :- First startup might took time becuase it wil downlaod trained model from cloud of size of 1.05gb approx.
