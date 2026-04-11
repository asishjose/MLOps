from flask import Flask, request, jsonify
import joblib
import os

app = Flask(__name__)

MODEL_PATH = os.path.join(os.path.dirname(__file__), "classifier.pkl")
model = joblib.load(MODEL_PATH)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)

    hours_studied = data["hours_studied"]
    attendance = data["attendance"]

    prediction = model.predict([[hours_studied, attendance]])[0]

    return jsonify({"prediction": int(prediction)})


if __name__ == "__main__":
    app.run(debug=True)
