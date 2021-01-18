from flask import Flask,render_template,url_for,request
from utils import predict_result
from query_filter import get_result
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    if request.form['options']=='text':
        sentence = request.form['tweet']
        tweet = predict_result(sentence)
        return render_template("prediction.html",data = tweet=="positive",sentence=sentence,dis="Your Tweet = ")
    else:
        sentence = request.form['tweet']
        res = get_result(sentence)
        return render_template("prediction.html",data = res=="positive",sentence=sentence,dis="Your Subject = ")

if __name__ == "__main__":
    app.run(debug=True)