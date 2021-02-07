from flask import Flask,render_template,url_for,request
from utils import retrieve_result
from query_filter import get_result
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    if request.form['options']=='text':
        sentence = request.form['tweet']
        res = retrieve_result(sentence)
        return render_template("prediction.html",data = res,sentence=sentence,dis="Your Tweet = ")
    else:
        sentence = request.form['tweet']
        res = get_result(sentence)
        return render_template("prediction.html",data = res=="positive",sentence=sentence,dis="Your Subject = ")

if __name__ == "__main__":
    port = int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)