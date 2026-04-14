from flask import Flask, request, jsonify
import os
import joblib

clsapp = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'classifier.pkl')
model = joblib.load(MODEL_PATH)

@clsapp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)

    hrs = data['hours_studied']
    att = data['attendance']

    result = model.predict([[hrs, att]])

    if result.tolist()[0] == 1:
        out = 'PASS'
    else:
        out = 'FAILED'
    return jsonify({'RESULT': out})

if __name__ == "__main__":
    clsapp.run(host="0.0.0.0", port=5000, debug=True)
