from flask import Flask, render_template,request
import pickle

#FLASK API
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        prediction_date_dict = request.form.to_dict()
        prediction_date = list(prediction_date_dict.values())[0]
        model = pickle.load(open('model.pkl','rb'))
        predicted_passengers = int(round(model.predict(prediction_date)[0],0))
        return render_template("result.html", prediction = predicted_passengers)


if __name__ == "__main__":
    app.run(debug=True)