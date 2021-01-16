from flask import Flask,render_template,url_for,request
from utils import predict_result
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=['POST'])
def predict():
    sentence = request.form['tweet']
    tweet = predict_result(sentence)
    return render_template("prediction.html",data = tweet[0]==1,sentence=sentence)

if __name__ == "__main__":
    app.run(debug=True)