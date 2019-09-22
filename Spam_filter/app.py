from flask import Flask,request,render_template
import pickle
from model import bow

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')



model = pickle.load(open('model.pkl','rb'))
#bow = CountVectorizer(lowercase=True,token_pattern='(?u)\\b\\w\\w+\\w',stop_words='english')



@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method =='POST':
        data = request.form['data']
        msg =[data]
        x = bow.transform(msg)
        result = model.predict(x)
        result = "".join(map(str, result))

    return render_template('home.html',result=result)



if __name__ == '__main__':
    app.run(debug=True,port=5000)

