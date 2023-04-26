import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
# prediction function


def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1, 7)
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    if request.method == 'POST':
        print(request.form)

        # time = request.args.get('time')
        # amount = request.args.get('amount')
        # tmethod = request.args.get('tm')
        # tid = request.args.get('ti')
        # ctype = request.args.get('ct')
        # location = request.args.get('location')
        # bank = request.args.get('em')

        # arr = [time, amount, tmethod, tid, ctype, location, bank]
        # print(arr)

        to_predict_list = request.form.to_dict()
        to_predict_list = list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        result = ValuePredictor(to_predict_list)
    if int(result) == 1:
        prediction = 'Given transaction is fradulent'
    else:
        prediction = 'Given transaction is NOT fradulent'
    return render_template("result.html", prediction=prediction)
    # return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
