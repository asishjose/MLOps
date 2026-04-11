from flask import Flask, request, jsonify
import os
import joblib

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "classifier.pkl")
model = joblib.load(MODEL_PATH)

@app.route("/predict", methods=['POST'])
def predict():
    data = request.get_json(force=True)

    hours_studied = data['hours_studied']
    attendance = data['attendance']

    result = model.predict([[hours_studied, attendance]])
    return jsonify(result.tolist())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
